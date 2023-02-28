from package.scrap_function import *
from package.firebase_function import put_data_to_firebase_demo,send_error

from datetime import datetime

import joblib
from package.scrap_function import *
import numpy as np

def word_split(text):
    words = re.split(r",",text)
    return words


def text_process_save_comma(text): ##save ,
    text = re.sub("\[|\]|'|"," ",text).replace(" ", "")
    text = re.sub(r'[0-9]+'," ",text) ##remove nember
    return text

##Load model
filename  = "prepare_dataset/model/check_type.sav"
filenamevector = "prepare_dataset/model/count_vectorizer.sav"
loaded_model = joblib.load(open(filename,"rb"))
vectorizer = joblib.load(open(filenamevector,"rb"))

timelist=["2020-07-10 10:38:42","2020-07-10 11:38:42","2020-07-10 12:38:42"]
u_name = 'BUBUMUMU'
u_id = '100008420610299'
url = 'https://m.facebook.com/photo/view_full_size'

txt_data = ["""หาหอห้องพัดลมราคา'2000-3000' บาท ครับ""",
"""ปล่อยบัตร paradox 1 ใบครับ 150บาท""",
"""ขายพัดลมหอเก่าไม่แพง 150 บาท""",
"เจอpencil powerbankหล่นหายหน้าตึกวิท"]

img = ['https://scontent.fhlz2-1.fna.fbcdn.net/v/t1.6435-9/fr/cp0/e15/q65/58745049_2257182057699568_1761478225390731264_n.jpg?_nc_cat=111&ccb=1-3&_nc_sid=8024bb&_nc_ohc=ygH2fPmfQpAAX92ABYY&_nc_ht=scontent.fhlz2-1.fna&tp=14&oh=7a8a7b4904deb55ec696ae255fff97dd&oe=60A36717',
       'https://cdn3.virtualsheetmusic.com/images/first_pages/HL-v/HL-319665First_BIG.png']
print('--------------------')


for i in range(1):
    start_time = datetime.now()
    text = cleanning(txt_data[i])
    print(text)
    print('--------------------')

    clean_txt_show = split_word(text)
    clean_txt_ai  = str(split_word(text))
    clean_txt_ai  = text_process_save_comma(clean_txt_ai)  ##clean number 
    text_list = vectorizer.transform([clean_txt_ai]).reshape(1,-1).todense()
    
    predictions = loaded_model.predict(np.asarray(text_list))
    post_type = predictions[0] ##0:FIND    1:SELL    2:OTHER

    try:
        if (post_type == 0):
            temp_dict = insert_data_to_dict("find",timelist[i],u_name,u_id,clean_txt_show,img,url)
        elif(post_type == 1):
            temp_dict = insert_data_to_dict("sell",timelist[i],u_name,u_id,clean_txt_show,img,url)
        elif(post_type==2):
            temp_dict = insert_data_to_dict("muuu",timelist[i],u_name,u_id,clean_txt_show,img,url)

        # find the detail of place & describe (color)
        if(post_type!=2):
            get_all_detail(clean_txt_show)
            check_empty(temp_place,temp_describe,temp_category) #if temp place,describe,category are empty it will fill with "-"

            #make data in list not duplicate            
            temp_place_rm_dp = [*set(temp_place)]
            temp_describe_rm_dp = [*set(temp_describe)]
            temp_category_rm_dp = [*set(temp_category)]

            print(f'temp_place = {str(temp_place_rm_dp)}\ntemp_describe = {str(temp_describe_rm_dp)}\ntemp_category =  {str(temp_category_rm_dp)}')
            # send data in temp_list to dict
            for data in temp_place_rm_dp:
                temp_dict["place"].extend({data})
            for data in temp_describe_rm_dp:
                temp_dict["describe"].extend({data})
            for data in temp_category_rm_dp:
                temp_dict["category"].extend({data})
            
        data_dict[timelist[i]] = temp_dict
        
        if(post_type!=2):
            time = str(temp_dict["date_time"])
            put_data_to_firebase_demo(time, temp_dict)

        #####clear list make sure its empty#####
        temp_place.clear()
        temp_describe.clear()
        temp_category.clear()
        #####clear list make sure its empty##### 

        end_time = datetime.now()
        print('\n\nDuration: {}\n\n'.format(end_time - start_time))
    except Exception as e:
        print(e)
        send_error(str(e))

# encode list to json
# jsonString = json.dumps(data_dict, ensure_ascii=False, indent=4, default=str)
# Writing to json
# writejson(jsonString)

# TODO TEST DATA_DICT
# print(data_dict)
