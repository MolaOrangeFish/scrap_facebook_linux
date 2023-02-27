import os
from datetime import datetime
import time
from make_json.package.firebase_function import update_time_to_firebase

def checktime():
    now = datetime.now()
    current_hour = now.strftime("%H")  #getcurrent time just usn only hour
    if(current_hour in ['18','06','17']): #เป็นเวลา หก เช้า หรือ หกเย็นมั้ย
        return True
    else:
        return False

flag = True
runtime = False

while(True):
    
    time.sleep(5)  #delay 5 sec in this demo we will use delay 10 min in real server
    print(checktime())
    runtime = checktime() 
    if(flag == True and runtime == True):
        for i in range(1,0,-1): #range(start,stop,step)
            print(f"Start Scaping in {i} Second(s).")
            time.sleep(1)
        os.system('pwd')
        # os.system('python make_json/main.py')
        os.system('python make_json/main_ai.py')
        os.system('python make_json/run_soup.py')
        now = datetime.now()
        current_time = now.strftime("%a %d %b %Y %H:%M")
        update_time_to_firebase(current_time)
        print(current_time )
        flag = False
    
