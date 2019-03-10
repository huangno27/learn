#!/usr/bin/python3
import requests
import datetime
import pymysql
from bs4 import BeautifulSoup

#连接数据库
db = pymysql.Connect('127.0.0.1', 'root', 'yuchen', 'douyu') #自行填充
cursor = db.cursor()
#获取斗鱼所有的直播分类
html = requests.get('https://www.douyu.com/directory')
soup = BeautifulSoup(html.text,'lxml')
li = soup.find_all('li')
#遍历所有的li标签
for tag in li:
    if tag.img and tag.div:
        href = 'https://www.douyu.com' + tag.a['href']
        name = tag.p.string
        r = requests.get(href)
        soup_1 = BeautifulSoup(r.text, 'lxml')
        p = soup_1.find_all('li')
        for i in p:
            try:
                if i.img:
                    room_url = 'https://www.douyu.com' + i.a['href']
                    zhubo_name = i.p.span.string
                    zhubo_looking = i.p.find_all('span')[1].string
                    room_title = i.h3.string.replace(' ', '')
                    looking = i.find_all('div')[2].find_all('span')
                    time_now = str(datetime.datetime.now())[:-7]
                    zhubo_tag = []
                    for n in looking:
                        zhubo_tag.append(n.string)
                    zhubo_tag = ','.join(zhubo_tag)
                    sql = "insert into gameinfo (游戏名称,主播,当前热度,房间标题," \
                          "主播标签,房间url,抓取时间) VALUES ('%s','%s','%s','%s'," \
                          "'%s','%s','%s')" % (name, zhubo_name, zhubo_looking,
                                               room_title, zhubo_tag, room_url, time_now)
                    cursor.execute(sql)
                    db.commit()
                    print(sql)
            except Exception:
                pass
db.close()