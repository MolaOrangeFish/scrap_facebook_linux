import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase import firebase
from datetime import datetime


##############################
#declare firebase config
# Fetch the service account key JSON file contents
cred = credentials.Certificate('make_json/kmutnbcommunity-firebase-adminsdk-s8kon-840841827e.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kmutnbcommunity-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
################################


#put data dict to firebase
def put_data_to_firebase(post_time:str,detail):
    year = post_time[0:4]
    month=post_time[5:7]
    url = "https://kmutnbcommunity-default-rtdb.asia-southeast1.firebasedatabase.app/"
    messenger = firebase.FirebaseApplication(url)
    messenger.put(f'/scraper/{year}/{month}',str(post_time),detail)

#####for demo#####
def put_data_to_firebase_demo(post_time:str,detail):
    year = post_time[0:4]
    month=post_time[5:7]
    url = "https://kmutnbcommunity-default-rtdb.asia-southeast1.firebasedatabase.app/"
    messenger = firebase.FirebaseApplication(url)
    messenger.put(f'/demo/{year}/{month}',str(post_time),detail)
#####for demo#####

##remove data
def remove_data_in_firebase(post_time:str):
    year = post_time[0:4]
    month=post_time[5:7]
    print("\n\nremoved\n\n")
    wanna_delete = db.reference(f"scraper/{year}/{month}/{post_time}")
    wanna_delete.delete()


def send_error(msg):
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y %H:%M:%S")
    url = "https://kmutnbcommunity-default-rtdb.asia-southeast1.firebasedatabase.app/"
    err_msg = firebase.FirebaseApplication(url)
    err_msg.put(f'/error',current_time,msg)


def update_time_to_firebase(post_time:str):
    url = "https://kmutnbcommunity-default-rtdb.asia-southeast1.firebasedatabase.app/"
    messenger = firebase.FirebaseApplication(url)
    messenger.put(f'/update_time/',"time",post_time)    