import requests
from lxml import etree
import ssl

url = "https://www.582tt.com/tupian/list-%E8%87%AA%E6%8B%8D%E5%81%B7%E6%8B%8D.html"
r = requests.get(url)
ret = r.content.decode()
#print(ret)
result = etree.HTML(ret)
#img = result.xpath('//*[@id="tpl-img-content"]/li[1]/a/img/@src')
img = result.xpath('//body[@class="videopic lazy"]/body/div/main/div/div/ul/li/a/img/@src')
# photo-content-title-text-main
# class="scroll-content"
# id="scroll-mian"
# /body/div/main/div/div/ul/
print(img)