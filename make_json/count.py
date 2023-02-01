from package.soup_function import *
count=0
year = db.reference("/scraper")
for y in year.get(): #Year
    # print(y)
    month = db.reference(f"/scraper/{y}")
    for m in month.get():  #Month
        # print(m)
        day = db.reference(f"/scraper/{y}/{m}")
        for d in day.get():
            # print(d)
            url = db.reference(f"/scraper/{y}/{m}/{d}/post_url").get()
            # print(url)
            count+=1
print(count)



###########################
## url_posttime_uid[0][0] : post url ##
## url_posttime_uid[0][1] : post time ##
## url_posttime_uid[0][2] : user_id ##
###########################
# print(url_posttime_uid[0][0])
# print(url_posttime_uid[1][0])
# print(url_posttime_uid[2][0])




###test zone###

# from package.soup_function_test import *
# from package.firebase_function import remove_data_in_firebase

# get_text_facebook()

# json_path = get_last_json_file()
# for file_name in json_path:
#     data_dict = convert_json_to_dict(file_name)
#     url_posttime_uid = get_data_in_data_dict(data_dict)  
#     get_text_facebook(url_posttime_uid)


###test zone###






