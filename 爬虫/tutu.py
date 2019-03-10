import requests
import re
# 找到url
url = "https://www.8989ee.com/html/news/69/"
# 解析url 获取网页源代码
r = requests.get(url)
# print(r)  返回 Response [200] response 代表一个对象 其中包括url 链接的数据
ret = r.content.decode()  # 二进制网页源代码的数据  decode代表字符串类型数据
#print(ret)    #对比源代码  是否一样
# 正则可以从字符串中提取我们想要的内容
# re.findall(正则表达式, 提取对象)
result = re.findall(r'//.+\.jpg', ret) # result 是一个列表类型
#print(result)
for i in result:
    #print(i)
    d = ("https:" + i)
    #print(d)
with open('tutu/%s' % d[-10:], "ab") as f:
    r = requests.get(d, timeout=3)
    f.write(r.content)

#www.135cd.com
#www.99bb9.com
#www.tianmi7.com
#www.pu310.com
