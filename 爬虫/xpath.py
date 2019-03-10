import requests
from lxml import etree
url = "https://www.baidu.com"
headers = {"User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
res = requests.get(url=url, headers=headers)
ret = res.content.decode()
#print(ret)
result = etree.HTML(ret) # 网页源码转换成xml 类型的数据

#content = result.xpath('//*[@id="u_sp"]/a[1]/text()') # xpath copy xpath 获取一条数据
content = result.xpath('//a[@href="http://news.baidu.com"]/text()')[0]

