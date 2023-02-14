from package.scrap_function import *
from package.firebase_function import put_data_to_firebase_demo,send_error

from datetime import datetime


time1 = "2020-05-10 16:38:42"
time2 = "2020-05-10 16:38:33"
u_name = 'BUBUMUMU'
u_id = '100008420610299'
url = 'https://m.facebook.com/photo/view_full_size'

txt_data = ["""
ขายสนใจหนังสือฟรีไหมส่งต่อน้า
""","เจอหูฟังหล่นหายหน้าตึก"]

img = ['https://scontent.fhlz2-1.fna.fbcdn.net/v/t1.6435-9/fr/cp0/e15/q65/58745049_2257182057699568_1761478225390731264_n.jpg?_nc_cat=111&ccb=1-3&_nc_sid=8024bb&_nc_ohc=ygH2fPmfQpAAX92ABYY&_nc_ht=scontent.fhlz2-1.fna&tp=14&oh=7a8a7b4904deb55ec696ae255fff97dd&oe=60A36717',
       'https://cdn3.virtualsheetmusic.com/images/first_pages/HL-v/HL-319665First_BIG.png']
print('--------------------')


for ex_txt in txt_data:
    start_time = datetime.now()
    text = cleanning(ex_txt)
    print(text)
    print('--------------------')

    clean_txt = split_word(text)
    print(clean_txt)
    post_type = get_post_type(clean_txt)

    if (post_type == "sell"):
        # create & insert data in to temp_dict_sell
        temp_dict = insert_data_to_dict("sell", time1, u_name, u_id, clean_txt, img, url)

        # find the detail of place & describe (color)
        get_all_detail(clean_txt)

        # make data in list not duplicate
        temp_place = list(set(temp_place))
        temp_describe = list(set(temp_describe))
        temp_category = list(set(temp_category))
        # send data in temp_list to dict
        for data in temp_place:
            temp_dict["place"].extend({data})
        for data in temp_describe:
            temp_dict["describe"].extend({data})
        for data in temp_category:
            temp_dict["category"].extend({data})

        time = str(temp_dict["date_time"])
        put_data_to_firebase_demo(time, temp_dict)

        data_dict["2020-05-10 16:38:42"] = temp_dict

        end_time = datetime.now()
        print('\n\nDuration: {}\n\n'.format(end_time - start_time))
    elif (post_type == "find"):
        # create & insert data in to temp_dict_find
        temp_dict = insert_data_to_dict("find", time2, u_name, u_id, clean_txt, img, url)

        # find the detail of place & describe (color)
        get_all_detail(clean_txt)

        # make data in list not duplicate
        temp_place = list(set(temp_place))
        temp_describe = list(set(temp_describe))
        temp_category = list(set(temp_category))
        # send data in temp_list to dict
        for data in temp_place:
            temp_dict["place"].extend({data})
        for data in temp_describe:
            temp_dict["describe"].extend({data})
        for data in temp_category:
            temp_dict["category"].extend({data})

        data_dict["2020-05-10 16:38:33"] = temp_dict
        time = str(temp_dict["date_time"])
        print("HELLLELAJ:LDKJASLD")
        put_data_to_firebase_demo(time, temp_dict)

        end_time = datetime.now()
        print('\n\nDuration: {}\n\n'.format(end_time - start_time))

    temp_category = temp_describe = temp_place = []

# encode list to json
# jsonString = json.dumps(data_dict, ensure_ascii=False, indent=4, default=str)
# Writing to json
# writejson(jsonString)

# TODO TEST DATA_DICT
print(data_dict)