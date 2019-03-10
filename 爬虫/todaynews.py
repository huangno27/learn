import requests
import re

news_url = "https://www.toutiao.com/ch/news_hot/"
headers = {
    "user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
    }
res = requests.get(news_url)
red = res.content.decode()
# print(red)
dingwei = re.findall('//div/a[@href="/group/6632237202006884878/"]>.*?</a>')

# r'//.+\.jpg'
# /html/body/div/div[4]/div[2]/div[2]/div/div/div/ul/li[1]/div/div[1]/div/div[1]/a
print(dingwei)