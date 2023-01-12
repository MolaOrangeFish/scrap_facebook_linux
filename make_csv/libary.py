import pandas as pd
from datetime import datetime
from facebook_scraper import get_posts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from pythainlp.tokenize.multi_cut import find_all_segment, mmcut, segment
from stop_words import get_stop_words
from nltk.corpus import words
from nltk.stem.porter import PorterStemmer
from pythainlp.corpus import thai_stopwords
from pythainlp.corpus import wordnet
from pythainlp.corpus import get_corpus
from pythainlp.util import normalize
from pythainlp import sent_tokenize, word_tokenize
import re
import string
import nltk
from datetime import datetime

# download stopword thai-eng
nltk.download('omw-1.4')
nltk.download('words')
th_stop_origin = tuple(thai_stopwords())
# append tuple thai stop word
th_stop = (th_stop_origin + ("สวัสดี", "ค่ะ", "เลย", "เรย","ๆ", "สุด", "นะคะ", "นะค่ะ", "ค่า", "อีกแล้ว","‼","⁉"))
en_stop = tuple(get_stop_words('en'))
p_stemmer = PorterStemmer()