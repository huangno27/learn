import requests
import re
import os

word = input('请输入你想要查的:')                   # word 替换url中word= 后边的内容
if not os.path.exists(word):                         # 如果路径下没有文件夹 就创建一个文件夹
    os.mkdir(word)
# 得到图片链接
url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1543582325085_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=LOL"
#start_url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1543582222278_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%B0%8F%E5%A7%90%E5%A7%90"
#      pn={}
#for k in range(10):
#    url = start_url.format(k * 60)      后面缩进

# 解析 url 得到网页源代码
r = requests.get(url)    #response [200] 200 状态码 response 的对象
# r.content() 得到网页源代码 她是2进制类型的数据
ret = r.content.decode() # 她是字符串类型的数据
#提取图片链接数据 这个时候必须是字符串类型数据
#正则表达式 能够从字符串里面把我们想要的数据都提取出来
#re.findall(正则表达式，提取对象)
#"objURL":""能后匹配到任何内容
result = re.findall('"objURL":"(.*?)",',ret)
# 保存图片
for i in result:
    # 创建一个文件，以w（write写入）b（二进制类型）的方法来写
    # 判断图片url结尾是否以图片类型结尾 如果不是 end 就等于 None
    end = re.search('(.jpg|.png|.gif|.jpeg)$',i)                       # i是url 地址
    if end == None:
        i = i + '.jpg'
    #从i[-10:] 里来查找元素替换为空的内容
    path = re.sub('','',i[-10:])

    try:

        with open('imgs/%s' % path,'wb') as f:
            r = requests.get(i,timeout=3)
            f.write(r.content)
    except Exception as e:
        print(e)
        pass
