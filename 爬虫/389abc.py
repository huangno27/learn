import requests
import re
url = "https://www.8989ee.com/html/news/69/"
r = requests.get(url)
ret = r.content.decode()
result = re.findall(r'//.+\.jpg', ret)
for i in result:
    d = ("https:" + i)
    #print(d)
with open("tutu/%s" % i[-10:],"ab") as f:
    rd = requests.get(d)#,timeout=3
    f.write(rd.content)

# 'tutu/%s' % d[-10:]
