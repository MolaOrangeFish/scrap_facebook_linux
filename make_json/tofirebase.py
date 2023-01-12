from package.firebase_function import *
from package.scrap_function import gettime
from package.libary import json

# Fetch the service account key JSON file contents
cred = credentials.Certificate(r'C:\Users\Corgi\Documents\GitHub\scappingFacebook\make_json\facebookscap-b297c-firebase-adminsdk-2af7k-8f6f9fab6e.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://facebookscap-b297c-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference("/")
ref.set({
	"scrap_data":-1    #-1 is set data to scrap_data

})

ref = db.reference("/scrap_data")

with open("make_json\log_json\scraping"+gettime()+".json", "r" ,encoding='utf-8') as f:
# with open("make_json\log_json\scraping_17-11-2022_15.json", "r" ,encoding='utf-8') as f:
	file_contents = json.load(f)

for key, value in file_contents.items():
	ref.push().set(value)

print(ref.get())
