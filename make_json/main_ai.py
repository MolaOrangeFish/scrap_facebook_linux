from package.nlp_function import *
from package.scrap_function import *
from package.firebase_function import *
from package.scrap_function import *
from facebook_scraper import get_posts
import numpy as np
import joblib
import json


def word_split(text):
    words = re.split(r",",text)
    return words


def text_process_save_comma(text): ##save ,
    text = re.sub("\[|\]|'|"," ",text).replace(" ", "")
    text = re.sub(r'[0-9]+'," ",text) ##remove nember
    return text


group_id = '197822284350539' #KMUTNB Community


##############Load model##############
filename  = "prepare_dataset/model/check_type.sav"
filenamevector = "prepare_dataset/model/count_vectorizer.sav"
loaded_model = joblib.load(open(filename,"rb"))
vectorizer = joblib.load(open(filenamevector,"rb"))
##############Load model##############

for post in get_posts(group=group_id, pages=3, extra_info=True, 
                      option={"comment": False,"posts_per_page": 3,"reactors": True},
                      credentials=("angpangsokawaii@gmail.com","angpangmanno1") #login facebook account
                      ):
    start_time = datetime.now()
    print('++++++++++++++++++++++++++++++++++++++++++++')
    text = cleanning(post['post_text'])
    print(text)

    clean_txt_show = split_word(text)
    clean_txt_ai  = str(split_word(text))
    clean_txt_ai  = text_process_save_comma(clean_txt_ai)  ##clean number 
    text_list = vectorizer.transform([clean_txt_ai]).reshape(1,-1).todense()
    predictions = loaded_model.predict(np.asarray(text_list))
    post_type = predictions[0] ##0:FIND    1:SELL    2:OTHER

    try:
        skip = False
        print(f"Predicted:{post_type}")
        if (post_type == 0):
            temp_dict = insert_data_to_dict("find",post['time'],post['username'],post['user_id'],clean_txt_show,post['images'],post['post_url'])
        elif(post_type == 1 and post['images'] != []):  #when you wanna sell you must have imgs
            temp_dict = insert_data_to_dict("sell",post['time'],post['username'],post['user_id'],clean_txt_show,post['images'],post['post_url'])
        elif(post_type == 1 and post['images'] == []):
            print("Skip sell post no pictures")
            skip = True
        # elif(post_type==2):
        #     temp_dict = insert_data_to_dict("muuu",post['time'],post['username'],post['user_id'],clean_txt_show,post['images'],post['post_url'])

        # find the detail of place & describe (color) if data is not 2
        if(post_type == 0 or post_type == 1 and skip == False):
            get_all_detail(clean_txt_show)
            check_empty(temp_place,temp_describe,temp_category) #if temp place,describe,category are empty it will fill with "-"

            #make data in list not duplicate            
            temp_place_rm_dp = list(set(temp_place))
            temp_describe_rm_dp = list(set(temp_describe))
            temp_category_rm_dp = list(set(temp_category))

            print(f'temp_place = {str(temp_place_rm_dp)}\ntemp_describe = {str(temp_describe_rm_dp)}\ntemp_category =  {str(temp_category_rm_dp)}')
            # send data in temp_list to dict
            for data in temp_place_rm_dp:
                temp_dict["place"].extend({data})
            for data in temp_describe_rm_dp:
                temp_dict["describe"].extend({data})
            for data in temp_category_rm_dp:
                temp_dict["category"].extend({data})

        #add all data 0,1 and 2 to data_dict for collecting data to make dataset for traing model   
        if skip == False:
            data_dict[str(post['time'])] = temp_dict
        
        #if data is not 2 will put data to firebase 
        if(post_type == 0 or post_type == 1 == False):
            time = str(temp_dict["date_time"])
            put_data_to_firebase(time, temp_dict)

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
#encode list to json
jsonString = json.dumps(data_dict,ensure_ascii=False, indent=4,default=str)
# Writing to json
writejson(jsonString)