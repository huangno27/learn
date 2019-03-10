import requests
import re
import os

word = input('请输入你想要查的:')
if not os.path.exists(word):
    os.mkdir(word)
# 1.找到图片链接
start_url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1543582325085_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word="+word+""

for k in range(10):
    start_url = start_url.format(k * 60)
# 2.解析url 得到网页源代码
r = requests.get(start_url)
ret = r.content.decode()

# 3.提取图片链接数据 用正则
result = re.findall('"objURL":"(.*?)",', ret)

# 4.保存图片
for i in result:
    print(i)
    end_name = re.search('(jpg|jpng|png)$',i)
    if end_name == None:
        i = i + '.jpg'
    path = re.sub('/','',i[-10:])
    try:
        with open('1/%s' % path, "ab") as f:
            r = requests.get(i, timeout=3)
            f.write(r.content)
            f.close()
    except Exception as e:
        print(e)
        pass