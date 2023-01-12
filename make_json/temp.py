from package.nlp_function import *
from package.scrap_function import *
from package.firebase_function import *

#dict
data_dict = {}
temp_dict_sell = {"date_time": {}, "username": {}, "user_id": {},"post_type": {}, "text": {}, 'image': [], 'post_url': {},'place':[],'describe':[],'category':[],'price':{}}
temp_dict_find = {"date_time": {}, "username": {}, "user_id": {},"post_type": {}, "text": {}, 'image': [], 'post_url': {},'place':[],'describe':[],'category':[]}
temp_place = []
temp_describe= []
temp_category = []

group_id = '197822284350539' #KMUTNB Community

for post in get_posts(group=group_id, pages=5, extra_info=True, option={"comment": False,"posts_per_page": 3,"reactors": True}):#group=group_id, pages=20,cookies="from_browser", extra_info=True, option={"comment": False,"posts_per_page": 3,"reactors": True}
    print('--------------------')
    originaltext = post['post_text']
    text = normalize (remove_emoji(post['post_text'])) # normalizeจัดการกับการพิมพ์ข้อความที่เรียงผิดหรือใช้ผิดอักษร เช่น "แ" พิมพ์เป็น "เ เ"
    print(text)
    print('--------------------')

    before_split = clean_msg(text)
    clean_txt = split_word(before_split)
    print("TEXT  :",(clean_txt))#type <class 'list'>
    try:
        for i in clean_txt:
            if (i in wanna_sell):
                # add data into temp_dict
                temp_dict_sell["date_time"] = post['time']
                temp_dict_sell["username"] = post['username']
                temp_dict_sell["user_id"] = post['user_id']
                temp_dict_sell["post_type"] = 'ขายของมือสอง'
                temp_dict_sell["text"] = clean_txt
                temp_dict_sell["image"] = post['images']
                temp_dict_sell["post_url"] = post['post_url']

                #get the price by find index of บาท  and get clean_txt[index-1]
                try:
                    index = clean_txt.index("บาท")
                    price = clean_txt[index-1]
                    temp_dict_sell["price"] = price
                except:
                    temp_dict_sell["price"] = "-"

                #find the detail of place & describe (color)
                for data in clean_txt:
                    data = data.lower() #make all word r in lower case 
                    cate = get_category(data)

                    place_list = db.reference('detail/place') #get place data list
                    color_list = db.reference('detail/color') #get place data list

                    if data in set(place_list):
                        temp_place.append(data)
                    elif data in set(color_list):
                        temp_describe.append(data)
                    else:
                        if cate is not None: #if category is match
                            temp_category.append(cate)

                #make data in list not duplicate            
                temp_place = set(temp_place)
                temp_describe = set(temp_describe)
                temp_category = set(temp_category)
                
                #send data in temp_list to dict
                for data in temp_place:
                    temp_dict_sell["place"].extend({data})
                for data in temp_describe:
                    temp_dict_sell["describe"].extend({data})
                for data in temp_category:
                    temp_dict_sell["category"].extend({data})


                # put data to firebase
                time = str(temp_dict_find["date_time"])
                put_data_to_firebase(time[0:4],time[5:7],time,temp_dict_sell["date_time"],temp_dict_sell)
                    
                # add temp_dict in to data_dect
                data_dict[str(post['time'])] = temp_dict_sell
                #empty temp_dict & temp_category
                temp_dict_sell = {"date_time": {}, "username": {}, "user_id": {},"post_type": {}, "text": {}, 'image': {}, 'post_url': {},'place':[],'describe':[],'category':[],'price':{}}
                temp_category = temp_describe = temp_place = []
                break
            elif(i in wanna_find):
                # add data into temp_dict
                temp_dict_find["date_time"]=post['time']
                temp_dict_find["username"] = post['username']
                temp_dict_find["user_id"] = post['user_id']
                temp_dict_find["post_type"] = 'ของหาย'
                temp_dict_find["text"] = clean_txt
                temp_dict_find["image"] = post['images']
                temp_dict_find["post_url"] = post['post_url']

                #find the detail of place & describe (color)
                for data in set(clean_txt):
                    data = data.lower() #make all word r in lower case 
                    cate = get_category(data)
                    place_list = db.reference('detail/place') #get place data list
                    color_list = db.reference('detail/color') #get place data list

                    if data in set(place_list.get()):
                        temp_place.append(data)
                    elif data in set(color_list.get()):
                        temp_describe.append(data)
                    else:
                        if cate is not None: #if category is match
                            temp_category.append(cate)
                #make data in list not duplicate            
                temp_place = set(temp_place)
                temp_describe = set(temp_describe)
                temp_category = set(temp_category)
                
                #send data in temp_list to dict
                for data in temp_place:
                    temp_dict_find["place"].extend({data})
                for data in temp_describe:
                    temp_dict_find["describe"].extend({data})
                for data in temp_category:
                    temp_dict_find["category"].extend({data})


                # put data to firebase
                time = str(temp_dict_find["date_time"])
                put_data_to_firebase(time[0:4],time[5:7],time,temp_dict_find)
                    
                # add temp_dict in to data_dect
                data_dict[str(post['time'])] = temp_dict_find
                #empty temp_dict & temp_category
                temp_dict_find = {"date_time": {}, "username": {}, "user_id": {},"post_type": {}, "text": {}, 'image': {}, 'post_url': {},'place':[],'describe':[],'category':[]}
                temp_category = temp_describe = temp_place = []

                break
        
    except Exception as e:
        send_error(str(e))

#encode list to json
jsonString = json.dumps(data_dict,ensure_ascii=False, indent=4,default=str)
# Writing to json
writejson(jsonString)


            