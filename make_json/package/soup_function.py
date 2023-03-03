import requests
from bs4 import BeautifulSoup
from package.nlp_function import *
from package.firebase_function import send_error,db,remove_data_in_firebase
from package.scrap_function import set_lower
from package.selenium_function import get_comment_facebooks

##Get text and use deepcut to split the word and check text 
def get_text_facebook(time,URL):
        print(f"URL:{URL}\nPosttime:{time}")
        try:
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")
                post_text = soup.div.p.text  ##Get post and check the text that have word mean this post that closed
                text = cleanning_except_emoji(post_text)
                split = split_word(text)
                print(f"Post_text  : {split}\n\n")
                check_post = check_close_post(split,"post") #will return not_found or found as str check the word "sold" in text list

                comment_text = get_comment_facebooks(URL) ##Get comment of poster and check the comment that have word mean this post that closed
                text = cleanning_except_emoji(comment_text)
                split = split_word(text)
                check_comment = check_close_post(split,"comment")
                if check_post == "found" or check_comment == "found": ##if in post or comment found word that mean like this post is colsed
                    print(f"#################\nFOUND delete data {time}\n#################")
                    # remove_data_in_firebase(time)
        except Exception as e:
            try: #try to remove again if error will send error to firebase 
                    remove_data_in_firebase(time)

            except:
                print(f"Error found::{e}")
                send_error(str(e))


def check_close_post(text_list,data_type):
    #make all char. to lower form
    text_list = set_lower(text_list)
    found_check = "not_found"
    if(data_type=="post"):
        bag_of_word = db.reference("close_post") #get the bag of word from firebase 
    elif(data_type=="comment"):
        bag_of_word = db.reference("close_post_comment") #get the bag of word from firebase 
    for word in set(bag_of_word.get()):
        if word in set(text_list):
            print(f"Close Found::{word}")
            found_check = "found"
    return found_check      
        


            

        


