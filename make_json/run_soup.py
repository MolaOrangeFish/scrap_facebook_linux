from package.soup_function import *
from package.firebase_function import remove_data_in_firebase

year = db.reference("/scraper")
##get in to all path and recheck the data in that path by get_text_facebook(d,url)
for y in year.get(): #Year
    month = db.reference(f"/scraper/{y}")
    for m in month.get():  #Month
        day = db.reference(f"/scraper/{y}/{m}")
        for d in day.get(): #day
            url = db.reference(f"/scraper/{y}/{m}/{d}/post_url").get()
            get_text_facebook(d,url)
print("Done checking closed post")