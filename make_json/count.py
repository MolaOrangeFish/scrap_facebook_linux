from package.soup_function import *

#count all data from firebase 

count=0
year = db.reference("/scraper")
for y in year.get(): #Year
    month = db.reference(f"/scraper/{y}")
    for m in month.get():  #Month
        day = db.reference(f"/scraper/{y}/{m}")
        for d in day.get():
            url = db.reference(f"/scraper/{y}/{m}/{d}/post_url").get()
            count+=1
print(count)

