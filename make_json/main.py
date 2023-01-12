from package.nlp_function import *
from package.scrap_function import *
from package.firebase_function import *
import pythainlp
from datetime import datetime


group_id = '197822284350539' #KMUTNB Community

for post in get_posts(group=group_id, pages=5, extra_info=True, option={"comment": False,"posts_per_page": 3,"reactors": True}):#group=group_id, pages=20,cookies="from_browser", extra_info=True, option={"comment": False,"posts_per_page": 3,"reactors": True}
    start_time = datetime.now()
    print('--------------------')
    text = cleanning(post['post_text'])
    print(text)
    print('--------------------')

    clean_txt = split_word(text)
    print("TEXT  :",(clean_txt))#type <class 'list'>
    post_type = get_post_type(clean_txt)
    try:
            if ( post_type == "sell"):
                ##create & insert data in to temp_dict_sell
                temp_dict = insert_data_to_dict("sell",post['time'],post['username'],post['user_id'],clean_txt,post['images'],post['post_url'])
                
                #find the detail of place & describe (color)  
                get_all_detail(clean_txt)

                #make data in list not duplicate            
                temp_place = set(temp_place)
                temp_describe = set(temp_describe)
                temp_category = set(temp_category)
                
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
                temp_dict = insert_data_to_dict("find",post['time'],post['username'],post['user_id'],clean_txt,post['images'],post['post_url'])

                #find the detail of place & describe (color)  
                get_all_detail(clean_txt)

                #make data in list not duplicate            
                temp_place = set(temp_place)
                temp_describe = set(temp_describe)
                temp_category = set(temp_category)
                
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
            temp_category = temp_describe = temp_place = []
            
    except Exception as e:
        send_error(str(e))

#encode list to json
jsonString = json.dumps(data_dict,ensure_ascii=False, indent=4,default=str)
# Writing to json
writejson(jsonString)


            