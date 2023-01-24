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
หอไหนติดเน็ตเองได้บ้างครับ ขอระแวก วงศ์สว่าง-พระราม 7"""

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


