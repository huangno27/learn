https://zhidao.baidu.com/question/40975924.html

import urllib.request
import re
# 1 获取主页源代码
# 2 获取章节超链接
# 3 获取章节超链接源码
# 4 获取小说内容
# 5 下载,文件操作

# 驼峰命名法
# 获取小说内容
def getNovertContent():
    # <http.client.HTTPResponse object at 0x000001DFD017F400>
    html = urllib.request.urlopen("http://www.quanshuwang.com/book/0/269").read()
    html = html.decode("gbk")
    # 不加括号  不匹配
    # 正则表达式  .*?  匹配所有
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    # 增加效率的
    reg = re.compile(reg)
    urls = re.findall(reg,html)
    # print(urls)
    # 列表
    # [(http://www.quanshuwang.com/book/0/269/78850.html,第一章 山边小村),
    # (http://www.quanshuwang.com/book/0/269/78854.html,第二章 青牛镇)]
    for url in urls:
        # 章节的URL地址
        novel_url = url[0]
        # 章节标题
        novel_title = url[1]

        chapt = urllib.request.urlopen(novel_url).read()
        chapt_html = chapt.decode("gbk")
        # r 表示原生字符串   \ \\d  r"\d"
        reg = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'
        # S 代表多行匹配
        reg = re.compile(reg,re.S)
        chapt_content = re.findall(reg,chapt_html)
        # print(chapt_content)
        # 列表["&nbsp;&nbsp;&nbsp;&nbsp二愣子睁大着双眼，直直望着茅草和烂泥糊成的<br />"]

        # 第一个参数   要替换的字符串   替换后的字符串
        chapt_content = chapt_content[0].replace("&nbsp;&nbsp;&nbsp;&nbsp;","")
        # print(chapt_content)    字符串  二愣子睁大着双眼，直直望着茅草和烂泥糊成的<br />
        chapt_content = chapt_content.replace("<br />","")

        print("正在保存 %s"%novel_title)
        # w 读写模式  wb
        # f = open("{}.txt".format(novel_title),'w')
        # f.write(chapt_content)

        with open("{}.txt".format(novel_title),'w') as f:
            f.write(chapt_content)

        # f.close()

getNovertContent()


import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3310,
    user='woider',
    passwd='3243',
    db='python',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

# 插入数据
sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
data = ('雷军', '13512345678', 10000)
cursor.execute(sql % data)
connect.commit()
print('成功插入', cursor.rowcount, '条数据')

# 修改数据
sql = "UPDATE trade SET saving = %.2f WHERE account = '%s' "
data = (8888, '13512345678')
cursor.execute(sql % data)
connect.commit()
print('成功修改', cursor.rowcount, '条数据')

# 查询数据
sql = "SELECT name,saving FROM trade WHERE account = '%s' "
data = ('13512345678',)
cursor.execute(sql % data)
for row in cursor.fetchall():
    print("Name:%s\tSaving:%.2f" % row)
print('共查找出', cursor.rowcount, '条数据')

# 删除数据
sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d"
data = ('13512345678', 1)
cursor.execute(sql % data)
connect.commit()
print('成功删除', cursor.rowcount, '条数据')

# 事务处理
sql_1 = "UPDATE trade SET saving = saving + 1000 WHERE account = '18012345678' "
sql_2 = "UPDATE trade SET expend = expend + 1000 WHERE account = '18012345678' "
sql_3 = "UPDATE trade SET income = income + 2000 WHERE account = '18012345678' "

try:
    cursor.execute(sql_1)  # 储蓄增加1000
    cursor.execute(sql_2)  # 支出增加1000
    cursor.execute(sql_3)  # 收入增加2000
except Exception as e:
    connect.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    connect.commit()  # 事务提交
    print('事务处理成功', cursor.rowcount)

# 关闭连接
cursor.close()
connect.close()