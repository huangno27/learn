import requests
import re
import pymysql
#timeout = 30

# conn = pymysql.connect(
#     host="localhost",        #ip
#     port=3306,        #端口
#     user="root",        #用户名
#     password="123456",      #密码
#     db="gameinfo",          #数据库名
#     charset="utf8" #编码
# )
config = {"host":"localhost",
          "user":"root",
          "password":"123456",
          "database":"Mysql"
          }
db = pymysql.connect(**config)

#使用cursor()方法创建一个游标对象
cursor = db.cursor()

#使用execute()方法执行SQL语句
cursor.execute("SELECT * FROM gameinfo")

#使用fetall()获取全部数据
data = cursor.fetchall()

#打印获取到的数据
print(data)

#关闭游标和数据库的连接
cursor.close()
db.close()