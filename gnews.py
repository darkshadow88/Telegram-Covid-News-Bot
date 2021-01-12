import requests
import read_token

config = "configG.cfg"
TOKEN = read_token.read_token_from_config_file(config)


def get_news():
    url = ('http://newsapi.org/v2/top-headlines?'
        'country=in&'
        'q=corona&'
        'sortBy=popularity&'
        'apiKey='+TOKEN)
    response = requests.get(url)
    x = response.json()
    news_source = []
    if x["status"]=="ok":
        y = x["articles"]
        for a in y:
            data={}
            data["news_source"] = a["source"]["name"]
            data["title"] = a["title"]
            data["link"] = a["url"]
            data["published_at"] = a["publishedAt"]
            news_source.append(data)
            # print(news_source+"\n"+title+"\n"+link+"\n"+published_at)
        return news_source

def get_msg(news_data):
    msg = "\n\n\n"
    for news_item in news_data:
        news_source = news_item["news_source"]
        title = news_item["title"]
        link = news_item["link"]
        published_at=news_item["published_at"]
        msg += title+'\n[<a href="'+link+'">source</a>]'+'\n<b>From:'+news_source+'</b>'
        msg += "\n\n"
        
    return msg

