import re
import requests

def getNoverSortList():
    response = requests.get("http://www.quanshuwang.com/list/1_1.html")
    response.encoding="gbk"
    result = response.text
    reg = r'<a target="_blank" title=".*?" href="(.*?)" class="clearfix stitle">(.*?)</a>'
    novel_url_list = re.findall(reg,result)
    #print(novel_url_list)                         # 获取列表 存有链接和书名
    return novel_url_list


# 获取开始阅读页面
def get_novel_content(url):
    response = requests.get(url)
    response.encoding='gbk'
    result = response.text
    #print(r)
    reg = '<a href="(.*?)" class="reader" title=".*?">开始阅读</a>'
    novel_url = re.findall(reg,result)[0]
    return novel_url



# # 获取章节页面
def get_chapter_url_list(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'<li><a href="(.*?)" title=".*?"</a></li>>'
    chapter_url_list = re.findall(reg,result)
    return chapter_url_list


# 获取小说内容
def get_chapter_content(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">style6'
    chapter_content = re.findall(reg, result, re.S)
    #print(chapt_content)
    return chapter_content

for novel_url,novel_name in getNoverSortList():
    novel_content_url = get_novel_content(novel_url)
    # 保存小说
    # cursor.execute("insert into novel1(name)VALUE ('{}')".format(novel_name))# 执行sql 语句
    # novelid = cursor.lastrowid # 拿到刚才存储的数据的 id
    #zhangjie_url_list = get_zhangjie_url_list(novel_conteng_url)
    for chapter_url,chapter_name in get_chapter_url_list(novel_content_url):
        get_chapter_content(chapter_url)
        print(chapter_url,chapter_name)