import requests
import re
import os

# word = input('请输入你想要查的:')                   # word 替换url中word= 后边的内容
# if not os.path.exists(word):                         # 如果路径下没有文件夹 就创建一个文件夹
#     os.mkdir(word)
# 1.找到图片链接
start_url = "https://www.toutiao.com/search/?keyword=火箭签约安东尼"
#
for k in range(10):
    start_url = start_url.format(k * 60)
    #print(start_url)
# 2.解析url 得到网页源代码
r = requests.get(start_url)
ret = r.content.decode()
# ctrl  + f 搜索 objURL 与网页源代码核对数据量 print(ret)
print(ret)

# 3.提取图片链接数据 用正则
result = re.findall('//div/a[@class="link title"]/text()', ret)
print(result) #确认为列表

# 4.保存图片
for i in result:
    print(i)
    end_name = re.search('(jpg|jpng|png)$',i)
    if end_name == None:
        i = i + '.jpg'
    path = re.sub('/','',i[-10:])
    try:
        with open('1/%s' % path, "ab") as f:
            r = requests.get(i, timeout=3)     # 这里取遍历得到的链接 i
            f.write(r.content)
            f.close()
    except Exception as e:
        print(e)
        pass

# https://blog.csdn.net/daxia5398/article/details/84106828