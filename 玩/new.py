import os
import requests
import re
#word = input('请输入你想要查的:')
#if not os.path.exists(word):
#   os.mkdir(word)

# 得到图片链接
url = "https://www.9696ss.com/"
r = requests.get(url)

ret = r.content.decode()

result = re.findall('"src":"(.*?)",',ret)
# 保存图片
for i in result:
    try:

        with open('imgk/%s' % i[-10:],'wb') as f:
            r = requests.get(i,timeout=3)
            f.write(r.content)
    except Exception as e:
        print(e)
        pass