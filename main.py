import requests
import send_email

api_key = '<API KEY>'
url = ("https://newsapi.org/v2/everything?"
       "domains=wsj.com"
       "&apiKey=8158c635d9174ea3bce6648c9e93eaae"
       "&language=en")
message = """\
Subject: Today's News


"""

request = requests.get(url)
content = request.json()
for article in content['articles'][0:20]:
    title = article['title']
    desc = article['description']
    nurl = article['url']
    message = f"{message}\n{title}\n{desc}\n{url}\n"

message = message.encode("utf-8")
send_email.send_message(message)
