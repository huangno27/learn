import requests
import bs4 import BeautifulSoup



url = 'http://www.autohome.com.cn/news/'
response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text,features='html.parser')
target = soup.finf(id = 'auto-channel-lazyload-article')
li_list = target.find_all('li')
for i in li_list:
    a = i.find('a')
    if a:
        print(a.attrs.get('href'))
        txt = a.find('h3')
        print(txt)
