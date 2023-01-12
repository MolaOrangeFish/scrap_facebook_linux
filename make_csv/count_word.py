from function import *

# dict
data_dict = {"date_time":[],"username":[],"user_id":[],"post_type":[],"text":[],'image':[],'post_url':[]}

ex_txt = '''คอนโดวิวโค้งน้ำเจ้าพระยา
Chapter one flow Bangpo
‼️โครงการใหม่‼️ ด่วนๆๆคนสนใจเยอะมาก
‼️ New Condo‼️
👇(Read more detail)👇
Review
https://youtu.be/yOw8QU_P0fE
✴️15,000 บาท/เดือน
https://line.me/ti/p/zTl2BJumXo
🏠ขนาดห้อง​ 45 ตร.ม. ชั้น33
River view 🌃
🌃1 ห้องนอน 1 ห้องน้ำ 1 ห้องครัว
1 ห้องอเนกประสงค์​ แอร์​ 2 ตัว
👍สิ่งอำนวยความสะดวกครบ  พร้อมหิ้วกระเป๋าเข้าอยู่
🚅 ห่างจาก MRT สีนำ้เงิน สถานีบางโพ​ เพียง​ 850m
🔌เครื่องใช้ไฟฟ้า​ + เฟอร์นิเจอร์
✨ของใหม่✨
✅เครื่องซักผ้า, ทีวี, ตู้เย็น, เเอร์, ไมโครเวฟ, เครื่องทำน้ำอุ่น, 
ฉากกั้นห้องน้ำ, Rain Shower, 
Digital Door Lock,
✅ บิวอินตู้เสื้อผ้า, โซฟา, เตียง, โต๊ะทานข้าว🍽
🌟พื้นที่ส่วนกลาง/สิ่งอำนวยความสะดวก
❇️สวนส่วนกลางขนาดใหญ่
❇️สระว่ายน้ำ, ฟิตเนส, ห้องสตรีม
❇️Study room, Party room
❇️ห้องประชุม, Sky lounge
❇️ร้านสะดวกซื้อ 7-11​, เครื่องซักผ้า​ ตู้กดน้ำหยอดเหรียญ, ตู้เต่าบิน,
ตู้เซ่เว่น
🛃รปภ. 24 ชั่วโมง, ที่จอดรถ
🛃ระบบคีย์การ์ด, กล้องวงจรปิด
👍สถานที่สำคัญใกล้เคียง😁
- รร.โยธินบูรณะ 100m
- รพ.บางโพ 900m
- เกทเวย์บางซื่อ 900m
-ท่าน้ำวัดสร้อยทอง 600m
-ท่าน้ำบางโพ 850m
- ม.เทคโนโลยีพระจอมเกล้าพระนครเหนือ​ 1.5km
- ม.เทคโนโลยีราชมงคลพระนคร​  วิทยาเขตพระนครเหนือ 1.5km
🎉เงื่อนไขการเช่า🎉
- ค่าเช่า 15,000บ./เดือน
- ค่าประกัน​ 2 เดือน
- ล่วงหน้า 1 เดือน
- สัญญาเช่า​ 1 ปี
⭕️ติดต่อนัดชมห้อง​ หรือสอบถามข้อมูลเพิ่มเติม
Inbox
โทร.093-579-3935(ทัน)
       084-690-7404(ป๊อป)
https://line.me/ti/p/zTl2BJumXo
Chapter one flow Bangpo
‼️New Condo‼️
💫High Rise Condominium 41 Floors, 1 Tower with 1 parking Tower and garden facility
-Elevator: 3 Passenger, 1 Service
-Parking area: 63%
👮‍♂️24 hours security
🛃 key card system, CCTV
🏠Room
-Size 43 sq.m
-Floor 33 
-River view
💸Price.
15,000 Bath/Month
410 $/Month
🛏1Bed, 🚿1Bath, 🍴1Kitchen, 1multipurpose room, 2 air conditioning
🤹‍♀️Facility
-SKY FACILITY
-LOBBY FACILITY
-STUDY ROOM
-GARDEN FACILITY
-LEISURE POOL
-MEETING ROOM
-LAUNDRY ROOM
-STREAM ROOM
👍 Ready to bring the bag in🤩
(taxi) Transportation
🚈 MRT Bangpo 850m
🚌 Dus stop 100m
🛳 Wan Soi Thong Pier 850m
🏥Hospital
-BANGPO HOSPITAL 
900m (3min)
-KASEMRAD PRACHACHUN
3.6km (10min)
-HOSPITAL YANHEE HOSPITAL
3km (10min)
🏢Department store
GATEWAY MALL
900m (3min)
CENTRAL LADPRAO
5km (15min)
THE MALL NGAMWONGWAN
5km (15min)
✨All new furniture✨
✅ Washing machine, TV, refrigerator, air conditioner, microwave, water heater,
 Bathroom partition, Rain Shower, Digital Door Lock
📌rental terms📌
- Rental fee 15,000 Bath/Month
- Room insurance 2 Month
- 1 month's rent in advance
- 1-year lease
⭕️Inbox ⭕️
Call.
084-690-7404 (Pop) / line
093-579-3935 (Thun) / line
https://line.me/ti/p/zTl2BJumXo'''
print('--------------------')
# normalizeจัดการกับการพิมพ์ข้อความที่เรียงผิดหรือใช้ผิดอักษร เช่น "แ" พิมพ์เป็น "เ เ"
text = normalize(remove_emoji(ex_txt))
# text = remove_emoji(ex_txt)
print(text)
print('--------------------')
before_split = clean_msg(text)
clean_txt = split_word(before_split)
# clean_txt = clean_msg(text)
print("TEXT  :", clean_txt)  # clean_txt type is list
# makedict(post['time'],post['user_id'],post['image'])
print("before_split:  ",clean_msg(text))
for i in clean_txt:
    if (i in ["ขาย","ส่งต่อ"]):
        print('ประกาศของซื้อขาย')
        data_dict["date_time"].extend(["2020-05-10 16:38:42"])
        data_dict["username"].extend(['BUBUMUMU'])
        data_dict["user_id"].extend(['100008420610299'])
        data_dict["post_type"].extend(['ประกาศของซื้อขาย'])
        data_dict["text"].extend([before_split])
        data_dict["image"].extend(['https://m.facebook.com/photo/view_full_size'])
        data_dict["post_url"].extend(['https://m.facebook.com/photo/view_full_size'])
        break
    elif(i in ["หาย", "รับคืน", "ลืม","หล่น"]):
        print('ประกาศของหาย')
        data_dict["date_time"].extend(["2020-05-10 16:38:42"])
        data_dict["username"].extend(['BUBUMUMU'])
        data_dict["user_id"].extend(['100008420610299'])
        data_dict["post_type"].extend(['ประกาศของหาย'])
        data_dict["text"].extend([before_split])
        data_dict["image"].extend(['https://m.facebook.com/photo/view_full_size'])
        data_dict["post_url"].extend(['https://m.facebook.com/photo/view_full_size'])
        break

    else:
        print("no")
        break



df = pd.DataFrame( data_dict)
print(df)
# Get csv file
# df.to_csv('scapping.csv', encoding='utf-8')
now = datetime.now()
current_time = now.strftime("_%d-%m-%Y_%H-%M-%S")
print(current_time)
# df.to_csv(r'C:\Users\kitti\Documents\GitHub\scappingFacebook\log_csv\scapping'+str(current_time)+'.csv', encoding='utf-8',index=False)

print("Save Complete...")
# print(type(clean_txt))


