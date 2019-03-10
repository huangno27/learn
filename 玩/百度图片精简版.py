import requests
import re
import os

word = input('请输入你想要查的:')
if not os.path.exists(word):
    os.mkdir(word)

url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1543582325085_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=LOL"

r = requests.get(url)
ret = r.content.decode()
result = re.findall('"objURL":"(.*?)",',ret)
for i in result:
    end = re.search('(.jpg|.png|.gif|.jpeg)$',i)
    if end == None:
        i = i + '.jpg'
    path = re.sub('','',i[-10:])
    try:
        with open('imgs/%s' % path,'wb') as f:
            r = requests.get(i,timeout=3)
            f.write(r.content)
    except Exception as e:
        pass