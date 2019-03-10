https://zhidao.baidu.com/question/40975924.html

import urllib.request
import re
# 1 ��ȡ��ҳԴ����
# 2 ��ȡ�½ڳ�����
# 3 ��ȡ�½ڳ�����Դ��
# 4 ��ȡС˵����
# 5 ����,�ļ�����

# �շ�������
# ��ȡС˵����
def getNovertContent():
    # <http.client.HTTPResponse object at 0x000001DFD017F400>
    html = urllib.request.urlopen("http://www.quanshuwang.com/book/0/269").read()
    html = html.decode("gbk")
    # ��������  ��ƥ��
    # ������ʽ  .*?  ƥ������
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    # ����Ч�ʵ�
    reg = re.compile(reg)
    urls = re.findall(reg,html)
    # print(urls)
    # �б�
    # [(http://www.quanshuwang.com/book/0/269/78850.html,��һ�� ɽ��С��),
    # (http://www.quanshuwang.com/book/0/269/78854.html,�ڶ��� ��ţ��)]
    for url in urls:
        # �½ڵ�URL��ַ
        novel_url = url[0]
        # �½ڱ���
        novel_title = url[1]

        chapt = urllib.request.urlopen(novel_url).read()
        chapt_html = chapt.decode("gbk")
        # r ��ʾԭ���ַ���   \ \\d  r"\d"
        reg = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'
        # S �������ƥ��
        reg = re.compile(reg,re.S)
        chapt_content = re.findall(reg,chapt_html)
        # print(chapt_content)
        # �б�["&nbsp;&nbsp;&nbsp;&nbsp�����������˫�ۣ�ֱֱ����é�ݺ�������ɵ�<br />"]

        # ��һ������   Ҫ�滻���ַ���   �滻����ַ���
        chapt_content = chapt_content[0].replace("&nbsp;&nbsp;&nbsp;&nbsp;","")
        # print(chapt_content)    �ַ���  �����������˫�ۣ�ֱֱ����é�ݺ�������ɵ�<br />
        chapt_content = chapt_content.replace("<br />","")

        print("���ڱ��� %s"%novel_title)
        # w ��дģʽ  wb
        # f = open("{}.txt".format(novel_title),'w')
        # f.write(chapt_content)

        with open("{}.txt".format(novel_title),'w') as f:
            f.write(chapt_content)

        # f.close()

getNovertContent()


import pymysql.cursors

# �������ݿ�
connect = pymysql.Connect(
    host='localhost',
    port=3310,
    user='woider',
    passwd='3243',
    db='python',
    charset='utf8'
)

# ��ȡ�α�
cursor = connect.cursor()

# ��������
sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
data = ('�׾�', '13512345678', 10000)
cursor.execute(sql % data)
connect.commit()
print('�ɹ�����', cursor.rowcount, '������')

# �޸�����
sql = "UPDATE trade SET saving = %.2f WHERE account = '%s' "
data = (8888, '13512345678')
cursor.execute(sql % data)
connect.commit()
print('�ɹ��޸�', cursor.rowcount, '������')

# ��ѯ����
sql = "SELECT name,saving FROM trade WHERE account = '%s' "
data = ('13512345678',)
cursor.execute(sql % data)
for row in cursor.fetchall():
    print("Name:%s\tSaving:%.2f" % row)
print('�����ҳ�', cursor.rowcount, '������')

# ɾ������
sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d"
data = ('13512345678', 1)
cursor.execute(sql % data)
connect.commit()
print('�ɹ�ɾ��', cursor.rowcount, '������')

# ������
sql_1 = "UPDATE trade SET saving = saving + 1000 WHERE account = '18012345678' "
sql_2 = "UPDATE trade SET expend = expend + 1000 WHERE account = '18012345678' "
sql_3 = "UPDATE trade SET income = income + 2000 WHERE account = '18012345678' "

try:
    cursor.execute(sql_1)  # ��������1000
    cursor.execute(sql_2)  # ֧������1000
    cursor.execute(sql_3)  # ��������2000
except Exception as e:
    connect.rollback()  # ����ع�
    print('������ʧ��', e)
else:
    connect.commit()  # �����ύ
    print('������ɹ�', cursor.rowcount)

# �ر�����
cursor.close()
connect.close()