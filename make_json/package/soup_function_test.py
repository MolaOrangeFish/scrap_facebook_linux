"""
import requests
import string
import json
import time
import glob
import os
from bs4 import BeautifulSoup
from facebook_scraper import get_posts
from package.nlp_function import *
from package.firebase_function import send_error,db,remove_data_in_firebase
from package.scrap_function import set_lower
from package.selenium_function import get_comment_facebooks





def get_text_facebook(time,URL):
    # URL = "https://m.facebook.com/groups/197822284350539/permalink/1165964820869609/"
    # URL = "https://m.facebook.com/groups/197822284350539/permalink/1246160679516689/" #test_post text
    # URL = "https://m.facebook.com/groups/197822284350539/permalink/1308622319937191/"  #test_comment

        # URL = "https://m.facebook.com/groups/197822284350539/permalink/1308622319937191/"
        # time = "2022-12-15 20:57:56"
        print(f"URL:{URL}\nPosttime:{time}")
        try:
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")
                post_text = soup.div.p.text  ##Get post_text 
                text = cleanning_except_emoji(post_text)
                split = split_word(text)
                print(f"Post_text  : {split}\n\n")
                check_post = check_close_post(split) #will return not_found or found as str check the word "sold" in text list

                comment_text = get_comment_facebooks(URL)
                text = cleanning_except_emoji(comment_text)
                split = split_word(text)
                check_comment = check_close_post(split)
                if check_post == "found" or check_comment == "found":
                    print(f"#################\nFOUND delete data {time}\n#################")
                    remove_data_in_firebase(time)
        except Exception as e:
            try:
                    remove_data_in_firebase(time)
            except:
                print(f"Error found::{e}")
                send_error(str(e))
                

def get_last_json_file():
    list_of_files = glob.glob('make_json/log_json/*.json') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    return list_of_files #make_json\log_json\scraping_26-12-2022_14.json


def convert_json_to_dict(path:str):
    # with open(path, "r", encoding='utf-8') as json_file:
    with open(path, "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def get_data_in_data_dict(data_dict):
    data_size = len(data_dict)
    data_list  = []
    temp_list = []
    for i in range(0,data_size):  #get url
            url = list(data_dict.values())[i]["post_url"]
            post_time = list(data_dict.values())[i]["date_time"]
            user_id = list(data_dict.values())[i]["user_id"]
            temp_list .append(url)
            temp_list .append(post_time)
            temp_list .append(user_id)
            data_list.append(temp_list)
            temp_list = []
    return data_list


def check_close_post(text_list):
    #make all char. lower form
    text_list = set_lower(text_list)
    found_check = "not_found"
    bag_of_word = db.reference("close_post")
    for word in set(bag_of_word.get()):
        if word in set(text_list):
            print(f"Close Found::{word}")
            found_check = "found"
    return found_check      
        
"""

            

        


