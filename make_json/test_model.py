import pickle
from package.scrap_function import *
from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn import *


def text_process(text):
    text = re.sub("\[|\]|'|,"," ",text)
    return text

filename  = "prepare_dataset/model/check_type.sav"
filenamevec = "prepare_dataset/model/vectorizer.sav"

loaded_model = pickle.load(open(filename,"rb"))
vectorizer = pickle.load(open(filenamevec,"rb"))

text = """
มีห้องว่างให้เช่า เดือนละ 3000 บาท รวมน้ำไฟแล้ว เลี้ยงสัตว์ได้
หมู่บ้านพิบูลย์บางซื่อ  เดินเข้ามอทางตึกบริหารได้
-ห้องอยู่ชั้น 3  ขนาด 3.5*3.5 เมตร มีระเบียง
-ห้องน้ำรวม มี 2 ห้อง ชั้น2 กับ ชั้น1
-ส่วนกลางมี ตู้เย็น 2 ตู้ เครื่องสักผ้า ครัว เตาไฟฟ้า เตาแก๊ส หม้อทอด ไมโครเวฟ
-เลี้ยงสัตว์ได้ ตอนนี้มี หมา2 แมว 1
-มีที่จอดรถ ทั้งมอไซค์ รถยนต์
-มีแอร์ของเจ้าของห้องเก่า (น่าจะเสีย)
-เป็นห้องเปล่าไม่มีเฟอร์
ทาวน์เฮ้าส์ 3 ชั้น 5นอน 2 น้ำ
ตอนนี้บ้านอยู่กัน 7 คน  ช 3 ญ 4   อยู่ได้ทั้งชายหญิง สนใจรายละเอียดเพิ่มเติมทักได้เลย"""

text = cleanning(text)
text = str(split_word(text))
text = text_process(text)

text_list = vectorizer.transform([text]).reshape(1,-1).todense()

print(text_list)
# my_bow = cvec.transform(pd.Series([my_tokens]))

# print(text_list)

# tvec = TfidfVectorizer()
# t_feat = tvec.fit_transform(text_list).todense()
# t_feat = np.array(t_feat)
# print(t_feat) 


my_predictions = loaded_model.predict(np.asarray(text_list))
if my_predictions[0] == 0:
    print("ของหาย")
elif my_predictions[0]==1:
    print("ขายของ")
else:
    print("ไม่เกี่ยวข้อง")


