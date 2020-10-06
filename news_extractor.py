import json
import requests

api_key = "a6b3d91efefd417f831ad57610d1aed5"
url = "https://newsapi.org/v2/top-headlines?country=us&apiKey={}".format(api_key)

responce = requests.get(url)
news_json = json.loads(responce.text)

count = 3 # Number Of News To Read

for news in news_json['articles']:
    if count>0:
        print("--------------------- News Title -------------------","\n")
        print(str(news['title']),"\n")
        print("--------------------- Description -------------------","\n")
        print(str(news['description']),"\n")
        count-=1