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

filename  = "prepare_dataset/model/check_type.sav"
filenamevec = "prepare_dataset\model\count_vectorizer.sav"

loaded_model = joblib.load(open(filename,"rb"))
vectorizer = joblib.load(open(filenamevec,"rb"))

text = """
ใครพบเห็น apple pencil 2 หายที่ห้อง78-316
 หายตอนเรียนช่วงเช้าใครเจอรบกวนติดต่อมาที
เบอร์ 0927023322นะครับ
"""

text = cleanning(text)
text = str(split_word(text))
text = text_process_save_comma(text)
print(text)
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


