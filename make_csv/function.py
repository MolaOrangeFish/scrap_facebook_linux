from libary import *
def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


def split_word(text):
    tokens = word_tokenize(text, engine='newmm')  # ลบคำฟุ่มเฟือยภาษาไทย

    # Remove stop words ภาษาไทย และภาษาอังกฤษ
    tokens = [i for i in tokens if not i in th_stop and not i in en_stop]

    # หารากศัพท์ภาษาไทย และภาษาอังกฤษ
    # English
    tokens = [p_stemmer.stem(i) for i in tokens]

    # Thai
    tokens_temp = []
    for i in tokens:
        # w_syn = wordnet.synsets(i)
        # if (len(w_syn) > 0) and (len(w_syn[0].lemma_names('tha')) > 0):
        #     tokens_temp.append(w_syn[0].lemma_names('tha')[0])
        # else:
        tokens_temp.append(i)

    tokens = tokens_temp

    # ลบตัวเลข
    # tokens = [i for i in tokens if not i.isnumeric()]

    # ลบช่องว่าง
    tokens = [i for i in tokens if not ' ' in i]

    return tokens


def clean_msg(msg):
    # ลบ text ที่อยู่ในวงเล็บ <> ทั้งหมด
    msg = re.sub(r'<.*?>', '', msg)
    # ลบ hashtag
    msg = re.sub(r'#', '', msg)
    # ลบ เครื่องหมายคำพูด (punctuation)
    for c in string.punctuation:
        msg = re.sub(r'\{}'.format(c), '', msg)
    # ลบ separator เช่น \n \t
    msg = ' '.join(msg.split())
    # ลบ link https
    msg = re.sub(r'http\S+', '', msg)

    return msg