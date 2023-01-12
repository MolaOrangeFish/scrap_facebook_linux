from function import *

#dict
data_dict = {"date_time":[],"username":[],"user_id":[],"post_type":[],"text":[],'image':[],'post_url':[]}

group_id = '197822284350539' #KMUTNB Community

for post in get_posts(group=group_id, pages=20, extra_info=True, option={"comment": False,"posts_per_page": 3,"reactors": True}):#group=group_id, pages=20,cookies="from_browser", extra_info=True, option={"comment": False,"posts_per_page": 3,"reactors": True}
    print('--------------------')
    originaltext = post['post_text']
    text = normalize (remove_emoji(post['post_text'])) # normalizeจัดการกับการพิมพ์ข้อความที่เรียงผิดหรือใช้ผิดอักษร เช่น "แ" พิมพ์เป็น "เ เ"
    print(text)
    print('--------------------')

    before_split = clean_msg(text)
    clean_txt = split_word(before_split)
    print("TEXT  :",(clean_txt))#type <class 'list'>
    try:
        for i in clean_txt:
            if (i in ["ขาย","ส่งต่อ"]):
                data_dict["date_time"].extend([post['time']])
                data_dict["username"].extend([post['username']])
                data_dict["user_id"].extend([post['user_id']])
                data_dict["post_type"].extend(['ประกาศของซื้อขาย'])
                data_dict["text"].extend([before_split])
                data_dict["image"].extend([post['image']])
                data_dict["post_url"].extend([post['post_url']])
                break
            elif(i in ["หาย", "รับคืน", "ลืม","หล่น"]):
                data_dict["date_time"].extend([post['time']])
                data_dict["username"].extend([post['username']])
                data_dict["user_id"].extend([post['user_id']])
                data_dict["post_type"].extend(['ประกาศของหาย'])
                data_dict["text"].extend([before_split])
                data_dict["image"].extend([post['image']])
                data_dict["post_url"].extend([post['post_url']])
                break
        df = pd.DataFrame(data_dict)
        print(df)
    except:
        print("exit with error")
#Get csv file
now = datetime.now()
current_time = now.strftime("_%d-%m-%Y_%H-%M-%S")
df.to_csv(r'C:\Users\kitti\Documents\GitHub\scappingFacebook\log_csv\scapping'+str(current_time)+'.csv', encoding='utf-8',index=False)
print("Save Complete...")

            