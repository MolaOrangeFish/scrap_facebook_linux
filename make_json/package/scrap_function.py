from package.libary import *
from package.nlp_function import *
from package.firebase_function import db

from facebook_scraper import get_posts
##insert data in to temp_dict
def insert_data_to_dict(post_type,time,u_name,u_id,txt,img,url):
    if post_type == "sell":  ##mean temp_dict_find
        data_dict = {"date_time": {}, "username": {}, "user_id": {},"post_type": {}, "text": {}, 'image': [], 'post_url': {},'place':[],'describe':[],'category':[],'price':{}}
        data_dict["date_time"] = time
        data_dict["username"] = u_name
        data_dict["user_id"] = u_id
        data_dict["post_type"] = 'ประกาศซื้อขาย'
        data_dict["text"] = txt
        data_dict["image"] = img
        data_dict["post_url"] = url
        #get the price by find index of บาท  and get clean_txt[index-1]
        try:
            try:
                index = txt.index("บาท")
                print(f"index::{index} ")
                price = txt[index-1]
                data_dict["price"] = price
            except:
                print("index not found")
                
            try:
                indexsym = txt.index("฿")
                print(f" indexsym::{indexsym}")
                price = txt[indexsym-1]
                data_dict["price"] = price
            except:
                print("indexsym not found")

        except:
            data_dict["price"] = "-"
    elif post_type == "find": ##mean temp_dict_sell
        data_dict = {"date_time": {}, "username": {}, "user_id": {},"post_type": {}, "text": {}, 'image': [], 'post_url': {},'place':[],'describe':[],'category':[]}
        data_dict["date_time"] = time
        data_dict["username"] = u_name
        data_dict["user_id"] = u_id
        data_dict["post_type"] = 'ประกาศของหาย'
        data_dict["text"] = txt
        data_dict["image"] = img
        data_dict["post_url"] = url
    elif post_type == "muuu":
        data_dict = {"date_time": {}, "username": {}, "user_id": {},"post_type": {}, "text": {}, 'image': [], 'post_url': {},'place':[],'describe':[],'category':[]}
        data_dict["date_time"] = time
        data_dict["username"] = u_name
        data_dict["user_id"] = u_id
        data_dict["post_type"] = 'mumu'
        data_dict["text"] = txt
        data_dict["image"] = img
        data_dict["post_url"] = url
    return data_dict


#find the detail of place & describe (color)
def get_all_detail(txt):
     for data in set(txt):
        data = data.lower()
        cate = get_category(data)

        place_list = db.reference('detail/place') #get place data list
        color_list = db.reference('detail/color') #get place data list
        if data in set(place_list.get()):
             temp_place.append(data)
        elif data in set(color_list.get()):
            temp_describe.append(data)
        else:
            if cate is not None:
                temp_category.append(cate)

    

##get category
def get_category(data):
    category = db.reference('detail/category')
    for cate_name in category.get(): ## {data_cate} get category <class 'str'>
        # print(f"\n\n\n{cate_name}\n\n\n") 
        cate_list = db.reference(f'detail/category/{cate_name}')
        if data in set(cate_list.get()): ## {ref.get()} get data in each category <class 'list'>
            return cate_name  ##return category as string

##get post_type
def get_post_type(data):
    post_type = db.reference("type")
    for char in data:
        for type_name in post_type.get():
            type_list = db.reference(f"type/{type_name}")
            if char in type_list.get():
                print(f"Found char::{char}\n\n")
                print(f"Found type::{type_name}\n\n")
                return type_name


#make all lower char
def set_lower(text_list):
    temp_list = []
    for i in text_list:
        temp_list.append(i.lower())
    return temp_list


#getting the time
def gettime():
    now = datetime.now()
    current_time = now.strftime("_%d-%m-%Y_%H")
    return current_time

#write json from dict
def writejson(data):
    #set time
    # Writing to json
    with open("make_json/log_json/scraping"+str(gettime())+".json", "a", encoding='utf-8') as outfile:
        outfile.write(data)
    print("Complete saving JSON...")