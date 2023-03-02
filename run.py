from make_json.package.firebase_function import update_time_to_firebase
from datetime import datetime
from check_connection import ping
import time
import os

def checktime():
    now = datetime.now()
    current_hour = now.strftime("%H")  #getcurrent time just use only hour
    if(current_hour in ['18','06']): #เป็นเวลา หก เช้า หรือ หกเย็นมั้ย
        return True
    else:
        return False

flag = True
runtime = False

while(True): 
    runtime = checktime() 
    if(flag == True and runtime == True and ping()==True):
        for i in range(3,0,-1): #range(start,stop,step)
            print(f"Start Scaping in {i} Second(s).")
            time.sleep(1)
        os.system('python make_json/main_ai.py')
        os.system('python make_json/run_soup.py')
        now = datetime.now()
        current_time = now.strftime("%a %d %b %Y %H:%M")
        update_time_to_firebase(current_time)
        print(current_time )
        flag = False
    else:
        os.system('cls') #clear screen
        ping_count=0
        if(ping()==False):
            if(ping_count==5):
                print("\nTaking a break 30 mins facebook.com can't be reach.\n")
                time.sleep(1800) #sleep for 30 mins
                
            print("\nPlease check network connection and try again.\n")
            time.sleep(10) #sleep 10 sec
            ping_count+=1

        elif(runtime==False):
            os.system('cls') #clear screen
            print("\nTaking a break 5 mins.\n")
            time.sleep(300) #sleep for 5 min

        
    
