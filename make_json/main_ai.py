from package.nlp_function import *
from package.scrap_function import *
from package.firebase_function import *
# import pythainlp
from datetime import datetime

import joblib
from package.scrap_function import *
from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

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


for post in get_posts(group=group_id, pages=3, extra_info=True, option={"comment": False,"posts_per_page": 3,"reactors": True}):#group=group_id, pages=20,cookies="from_browser", extra_info=True, option={"comment": False,"posts_per_page": 3,"reactors": True}
    start_time = datetime.now()
    print('++++++++++++++++++++++++++++++++++++++++++++')
    text = cleanning(post['post_text'])
    print(text)

    clean_txt_show = split_word(text)
    print(clean_txt_show)
    clean_txt_ai  = str(split_word(text))
    clean_txt_ai  = text_process_save_comma(clean_txt_ai)  ##clean number 
    text_list = vectorizer.transform([clean_txt_ai]).reshape(1,-1).todense()
    print(text_list)
    predictions = loaded_model.predict(np.asarray(text_list))
    post_type = predictions[0] ##0:FIND    1:SELL    2:OTHER
    try:
            if ( post_type == 1):
                ##create & insert data in to temp_dict_sell
                temp_dict = insert_data_to_dict("sell",post['time'],post['username'],post['user_id'],clean_txt_show,post['images'],post['post_url'])
                
                #find the detail of place & describe (color)  
                get_all_detail(clean_txt_show)

                #make data in list not duplicate            
                temp_place = list(set(temp_place))
                temp_describe = list(set(temp_describe))
                temp_category = list(set(temp_category))
                
                print(f'temp_place = {str(temp_place)}\ntemp_describe = {str(temp_describe)}\ntemp_category =  {str(temp_category)}')
                
                #send data in temp_list to dict
                for data in temp_place:
                    temp_dict["place"].extend({data})
                for data in temp_describe:
                    temp_dict["describe"].extend({data})
                for data in temp_category:
                    temp_dict["category"].extend({data})


                # put data to firebase
                time = str(temp_dict["date_time"])
                put_data_to_firebase(time,temp_dict)
                    
                # add temp_dict in to data_dect
                data_dict[str(post['time'])] = temp_dict
                
                #measure the time
                end_time = datetime.now()
                print('\n\nDuration: {}\n\n'.format(end_time - start_time))
                # break
            elif(post_type == "find"):
                # add data into temp_dict
                temp_dict = insert_data_to_dict("find",post['time'],post['username'],post['user_id'],clean_txt_show,post['images'],post['post_url'])

                #find the detail of place & describe (color)  
                get_all_detail(clean_txt_show)

                #make data in list not duplicate            
                temp_place = list(set(temp_place))
                temp_describe = list(set(temp_describe))
                temp_category = list(set(temp_category))
                
                #send data in temp_list to dict
                for data in temp_place:
                    temp_dict["place"].extend({data})
                for data in temp_describe:
                    temp_dict["describe"].extend({data})
                for data in temp_category:
                    temp_dict["category"].extend({data})
                print(f'temp_place = {str(temp_place)}\ntemp_describe = {str(temp_describe)}\ntemp_category =  {str(temp_category)}')

                # put data to firebase
                time = str(temp_dict["date_time"])
                put_data_to_firebase(time,temp_dict)
                    
                # add temp_dict in to data_dect
                data_dict[str(post['time'])] = temp_dict

                #measure the time
                end_time = datetime.now()
                print('\n\nDuration: {}\n\n'.format(end_time - start_time))
                # break
            else:
                # add data into temp_dict
                temp_dict = insert_data_to_dict("muuu",post['time'],post['username'],post['user_id'],clean_txt_show,post['images'],post['post_url'])

                #find the detail of place & describe (color)  
                # get_all_detail(clean_txt)

                # put data to firebase
                time = str(temp_dict["date_time"])
                # put_data_to_firebase(time,temp_dict)
                    
                # add temp_dict in to data_dect
                data_dict[str(post['time'])] = temp_dict

                #measure the time
                end_time = datetime.now()
                print('\n\nDuration: {}\n\n'.format(end_time - start_time))
                # break
            temp_category = temp_describe = temp_place = []
    except Exception as e:
        send_error(str(e))

#encode list to json
jsonString = json.dumps(data_dict,ensure_ascii=False, indent=4,default=str)
# Writing to json
writejson(jsonString)


            