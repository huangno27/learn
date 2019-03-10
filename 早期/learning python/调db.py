import pymysql
pymysql.install_as_MySQLdb()
_author_ = 'pythontab.com'
import pymysql
try:
    conn = pymysql.connect(host="localhost", user='root',passwd='huangy',db='pythontab',port=3306,charset='utf8')
    cur = conn.cursor()
    cur.execute('select * from user')
    data=cur.fetchall()
    for d in data :
        print("ID: "+str(d[0])+'  用户名： '+d[1]+"  注册时间： "+d[2])
    cur.close()#关闭游标
    conn.close()#释放数据库资源
except Exception : print("查询失败")

