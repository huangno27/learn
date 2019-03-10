import requests
import re
from lxml import etree


# 获取小说目录 目录页面源代码
# 获取章节href
# 获取小说章节内容
# 下载小说

def getBookContent():

    #获取小说目录
    mulu_url = "https://book.qidian.com/info/1209977#Catalog"
    #http://m.qidian.com/book/showbook.aspx?bookid=1209977
    #提交url 获取页面源代码
    mulu_html = requests.get(mulu_url).text         # 获取解码格式
    # mulu_url = requests.get(mulu_url).content     # 获取未解码格式
    #print(mulu_html)                                 # 文本类型

    # 获取目录章节
    # 正则表达式获取
    reg = '<li><a href="(.*?)">.*?</a></li>'    # 加括号是想要的内容  #
    # //*[@id="j-catalogWrap"]/div[2]/div[1]/ul/li[1]/a
    urls = re.findall(reg,mulu_html)
    print(urls)

    # 获取小说章节的超链接&章节名称
    for i in urls:
        chapt_title = i[1]
        chapt_url=mulu_url+i[0]
        # 获取章节内容
        chapt_html = requests.get(chapt_url).content.decode("UTF-8")   # 源码content_type 对应的格式  charset=gbk
        chapt_html = etree.HTML(chapt_html)                           # 转译
        chapt_pipei = chapt_html.xpath('//*[@id="j_chapterBox"]/text()') #   //*[@id="htmlContent"]/text()
        # xpath 找id
        #print(chapt_pipei)                 #\xa0 是空格
        #print(chapt_url)
        print(chapt_html)

        # 下载小说
        f = open(r'C:\Users\acer\PycharmProjects\learn\read.txt'.format(chapt_title),'w')
        for a in chapt_pipei:         # 去掉空格
            a = a.replace("\xa0","")
            print(a)
            f.write(a)
            f.write("\r\n")   #转换成小说格式 不然会在一行显示内容
        f.close()
        print("%s写入结束！！！"%chapt_title)

getBookContent()

# https://book.qidian.com/info/1209977#Catalog
# https://m.qidian.com/book/1209977

