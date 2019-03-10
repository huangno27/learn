import requests
import re
import pymysql
timeout = 30

conn = pymysql.connect(
    host="localhost",        #ip
    port=3306,        #端口
    user="root",        #用户名
    passwd="123456",      #密码
    db="gameinfo",          #数据库名
    charset="utf8" #编码
)
# # 建立游标
cursor = conn.cursor()
# 出现乱码的原因是显示的编码与原始字符编码不一致
# 解决办法是统一编码类型

url = "http://www.quanshuwang.com/list/1_1.html"


def getNoverSortList():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
                }
    response = requests.get(url=url, headers=headers)
    response.encoding="gbk"
    result = response.text
    #print(result)
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
    print(novel_url)
#     #return novel_url



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
    #print(novel_url,novel_name)
    #get_novel_content(novel_url)  # 为第二个def确认
    #get_chapter_url_list(novel_content_url)
    novel_content_url = get_novel_content(novel_url)
    # 保存小说
    cursor.execute("insert into novel1(name) values(%s)".format(novel_name))# 执行sql 语句
    novelid = cursor.lastrowid # 拿到刚才存储的数据的 id
#    zhangjie_url_list = get_zhangjie_url_list(novel_conteng_url)
    for chapter_url,chapter_name in get_chapter_url_list(novel_content_url):
        chapter_content = get_chapter_content(chapter_url)
        cursor.execute("INSERT INTO chapter1(name,content,novelid)VALUES (%s,%s,%s)  #('{}','{}',{})"
                       .format(chapter_name,chapter_content,novelid))
        conn.commit()
cursor.close()
conn.close()

# https://www.cnblogs.com/W-Kr/p/5456810.html
