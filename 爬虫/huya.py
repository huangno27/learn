#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import pymysql
import re
import datetime

db = pymysql.Connect('127.0.0.1', 'root', 'yuchen', 'huya')
cursor = db.cursor()

html = requests.get('https://www.huya.com/g')
soup = BeautifulSoup(html.text,'lxml')
li = soup.find_all('li')

for i in li:
    try:
        url = i.a['href']
        if i.h3.string:
            name = i.h3.string
            yy = requests.get(url)
            soup_2 = BeautifulSoup(yy.text, 'lxml')
            p = soup_2.find_all('li')
            for n in p:
                if n.img:
                    room_url = n.a['href']
                    zhubo_name = n.img['alt'][0:-3]
                    room_title = n.find_all('a')[1].string
                    looking = n.find_all('span')[2].find_all('i')[1].string
                    r = requests.get(room_url)
                    soup_1 = BeautifulSoup(r.text, 'lxml')
                    div = soup_1.find_all('div')
                    a = re.search('Count.*<', r.text).group()[7:-1]
                    time_now = str(datetime.datetime.now())[:-7]
                    sql = "insert into gameinfo (游戏名称,主播,房间标题,当前观看量," \
                          "当前订阅量,房间url,抓取时间) VALUES ('%s','%s','%s','%s'" \
                          ",'%s','%s','%s')" % (
                    name,zhubo_name,room_title,looking,a,room_url,time_now)
                    cursor.execute(sql)
                    db.commit()
                    print(sql)
    except Exception:
        pass
db.close()