import pymysql

# 获取连接方法
# def get_db_conn():
#     conn = pymysql.connect(
#
#     )
#     return conn
#
# # 封装数据库查询操作
# def query_db(sql):
#     conn = getattr() #获取连接
#     cur = conn.cursor() # 建立游标
#     cur.execute(sql) # 执行sql
#     result = cur.fetchall()  # 获取所有查询
#     cur.close()
#     conn.close()
#     return result
#
# # 封装更改数据库操作
# def change_db(sql):
#     conn = getattr()  # 获取连接
#     cur = conn.cursor()  # 建立游标
#     try:
#         cur.execute(sql) # 执行sql
#         conn.commit()
#     except Exception as e:
#         conn.rollback() # 回滚
#     finally:
#         cur.close()
#         conn.close()
#
# # 封装数据库常用操作
# def check_uesr(name):
#     # 注意sql中''号嵌套的问题
#     sql = "select * from user where name = '{}'".format(name)
#     result = query_db(sql)
#     return True if result else False
#
# def add_user(name,password):
#     sql = "insert into user(name,passwd) values('{}','{}')".format(name,password)
#     change_db(sql)
#
# def def_user(name):
#     sql = "delete from user where name='{}'".format(name)
#     change_db(sql)


class DB:
    def __init__(self):
        self.conn = pymysql.connect(host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = '123456',
        charset = 'utf8')
        self.cur = self.conn.cursor()

    def __del__(self): # 析构函数 实例删除时触发
        self.cur.close()
        self.conn.close()

    def query(self):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def check_user(self,name):
        result = self.query("select * from user where name = '{}'".format(name))
        return True if result else False

    def del_uesr(self,name):
        self.exec("delete from user where name='{}'".format(name))

