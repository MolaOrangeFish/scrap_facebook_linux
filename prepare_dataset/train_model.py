from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from function import str_to_list

df = pd.read_csv('new_data.csv')
size = df.shape[0]

# text = df['text'][0]
# text_list = str_to_list(text)
# print(text_list)
# print(len(text_list))
for i in range(0,5):
    text = df['text'][i]
    text_list = str_to_list(text)
    tvec = TfidfVectorizer(analyzer=lambda x:x.split(','),)
    t_feat = tvec.fit_transform(text_list)

    print(t_feat[:,:5].todense())
    print(len(tvec.idf_),len(tvec.vocabulary_))