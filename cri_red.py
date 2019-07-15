import praw
import random
import re
import requests
from termcolor import colored

def telegram_bot_sendtext(bot_token,bot_chatID,bot_message):

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()




colors = ["red","yellow","green","magenta","cyan","white","blue"]

count = 0
reddit = praw.Reddit(client_id='477ySXxt3C4kNQ',
                     client_secret='MisKIal4KHnj2mf8Sp4fKu4H7Ko', password='Alzeimers@14',
                     user_agent='PrawTut', username='thenikkkhil')


for comment in reddit.subreddit('cricket').stream.comments():
# for comment in reddit.subreddit('cricket').stream.comments(skip_existing=True):
    count +=1
    canvas = random.choice(colors)
    # print(colored(count,canvas ), colored('.', canvas),  colored(comment.body, canvas))
    links =  re.findall(r'(https?://[^\s]+)', comment.body)
    if len(links) == 0:
        print(colored(count,canvas ), colored('.', canvas),  colored(comment.body, canvas))
        test = telegram_bot_sendtext('874736358:AAHAJpiYI8zShXVHU6BlAsJMXODdbSDruNo','609735179',comment.body)
    else:
        for i in links:
            test = telegram_bot_sendtext('814952229:AAG9a3eN-qJg5LNcqPZSitoPBWEztCxR7G0','609735179',i)
            print(test)
            print("links",i)

    # if len(links) != 0:
    #     for i in links:
    #         test = telegram_bot_sendtext('814952229:AAG9a3eN-qJg5LNcqPZSitoPBWEztCxR7G0','609735179',i)
            # print(test)
    #         # print("links",i)
    # else:
    #     print(colored(count,canvas ), colored('.', canvas),  colored(comment.body, canvas))
    #     test = telegram_bot_sendtext('874736358:AAHAJpiYI8zShXVHU6BlAsJMXODdbSDruNo','609735179',comment.body)
