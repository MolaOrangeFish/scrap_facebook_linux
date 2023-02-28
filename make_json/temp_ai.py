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


for i in range (1):
    start_time = datetime.now()
    print('++++++++++++++++++++++++++++++++++++++++++++')
    txt="""ประกาศขายสัญญาหอครับ
หอ : Soul Dormitory
 เตียง+ที่นอน 5ฟุต 
ชั้นวางหนังสือ +ชั้นวางรองเท้า 
โต๊ะอ่านหนังสือพร้อมเก้าอี้2ตัว
ตู้เสื้อผ้า 
ราวตากผ้า 
ตู้เย็น 
internet 30MB /ห้อง (1 ห้อง 1 เลาว์เตอร์)
แอร์
เครื่องทำน้ำอุ่น
เลี้ยงแมวได้นะครับ(สอบถามเพิ่มเติมได้ครับ)
น้ำ : 18
ไฟฟ้า : 8
ราคาค่าเช่าเดือนละ 6000 บาท
ราคาสัญญา 10,000 บาท (ต่อรองได้)
พร้อมให้เข้าอยู่เดือน เมษายน
สัญญาสิ้นสุด มิถุนายน
สนใจติดต่อได้เลยครับ
รูปภาพเพิ่มเติม : https://m.facebook.com/story.php?story_fbid=132808184980704&id=104802554447934&mibextid=tejx2t"""
    text = cleanning(txt)
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
                temp_dict = insert_data_to_dict("sell",'2023-02-26 15:46:01','Gup Guthai','100006907245716',clean_txt_show,'https://scontent.fbkk29-4.fna.fbcdn.net/v/t1.6435-9/92675026_132807924980730_4876351154566463488_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=111&ccb=1-7&_nc_sid=110474&_nc_ohc=9yjsL2OPB2QAX_5Fh26&_nc_ht=scontent.fbkk29-4.fna&oh=00_AfBxCnDuUTpJjAabvSW76He5wm8fys2QxOPbi4Oc2gWFjg&oe=64244AC4','https://m.facebook.com/groups/197822284350539/permalink/1357976188335137/')
                
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
                put_data_to_firebase_demo(time,temp_dict)
                    
                # add temp_dict in to data_dect
                data_dict['2023-02-26 15:46:01'] = temp_dict
                
                #measure the time
                end_time = datetime.now()
                print('\n\nDuration: {}\n\n'.format(end_time - start_time))

            temp_category = temp_describe = temp_place = []
    except Exception as e:
        send_error(str(e))

#encode list to json
# jsonString = json.dumps(data_dict,ensure_ascii=False, indent=4,default=str)
# Writing to json
# writejson(jsonString)


            