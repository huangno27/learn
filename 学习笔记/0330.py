# coding utf-8
emelet_ingredients = {"egg":2, "pepper":5, "mush":5}
fridge_contents = {"egg":10, "pepper":2, "mush":6}
having_ingredients = [False]
if fridge_contents["egg"] > emelet_ingredients["egg"]:   #如果第一个if不为真 他下面的任何代码都不会被求值而将被完全跳过
    having_ingredients[0] = True
    having_ingredients.append("egg")
print(having_ingredients)
if fridge_contents["mush"] > emelet_ingredients["mush"]:
    if having_ingredients[0] == False:                   #如果第一个if为真，同级的第二个条件将被计算
        having_ingredients[0] == True
        having_ingredients.append("mush")
print(having_ingredients)

a = 10
b = 20
print("A added to B is %s :" % (a + b))

def in_fridge():

    try:
        count = fridge[wanted_food]
    except KeyError:
        count = 0
    return count

fridge = {"apples":10, "oranges":5, "milk":20}
wanted_food = 'apples'
in_fridge()

def hanshu(hsmc):
    "打印传入的函数到显示器"
    hanshu_renyi               #函数体
    return[chenggong]          #return值
#定义函数的三种形式
#无参函数：当函数体内代码无需外部传入参数就可能执行，那就定义成无参函数
     def func(x):
         pass
#有参函数：当函数体内代码需要外部传入参数才可以执行，那就定义有参函数
      def func(x):
          print(x)
#空函数
      def fun():
          pass

def func()                        #语句形式
    res = func2(10)               #表达式
    res = 10*func2(10)

    res = func2(func2(10))         #函数调用当做参数传入另外一个函数

def func(d):
    if count == d_doo:
        return "成功"
    else:
        return "失败"
#先定义，后使用，定义阶段只判断语法，不执行代码。上面定义阶段 if 1>2 print……有语法错误，所以报错，下面，调用了不存在的变量，不算语法错误
d = {"a":1, "b":2, "c":3}
d_doo = 'a'

dim = (200, 50)
print("Org dimensons:")
for dimenson in dim:
    print(dimenson)
dim = (400, 100)
print("\nModified dim:")
for dimension in dim:
    print(dimension)


zzc = ("milk", "ac","ad", "ap", "mod" )
for chi in zzc:
    print(zzc)
    break                                  #将自助餐提供的五种食品都打印出来 并且只打印一次 去掉break会打印五次

zzc_c = ("milk", "ac", "ad", "ap",{'k1':'v1','k2':'v2'})
for chi in zzc_c:
    print(zzc_c)
    break
zzc_c = ("milk", "ac", "ad", "ap",{'k1':'v1','k2':'v2'})
zzc_c[4]['k1'] = 'bian1'                    #元组里的元素是不可变的，但是元组的元素的元素是可变的
for chi in zzc_c:
    print(zzc_c)
    break




zzc = ("milk", "ac","ad", "ap", "mod" )
zzc.index[0] = 'cd'                         #元组不能修改其中的一个元素
print(zzc)


a = ("1", "2", "3")
bd = ("23", "12")
a = (bd, "1", "2", "3")
print(a)


zzc = ("a", "v", "s", "d", "g")            #重新定义元组会占用内存 不是最优办法
for chang in zzc:
    break
zzc = ("a", "v", "s", "k", "t")
for chang in zzc:
    print(chang)

zzc_l = ("a", "i","s", {"k1":2, "t2":3})    #元组里加列表 替换赋值
for lunch in zzc_l:
    print(lunch)
zzc_l[3]['k1'] = 'x3'
#zzc_l[4]['t2'] = 'b4'                     #修改时只能先修改一条
for lunch in zzc_l:
    print(lunch)
    #print("这种方法")

cars = ["audi", "bmw", "auto", "infiniti"]
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

cars = ["ak", "bk", "ced"]             #for 循环 in 条件判断
for dd in cars:
    if "da" in cars:
        print("对对对")
        break
    else:
        print("buzai")
        break


car_nm = ["ak", "ds", "dj"]           #in方法能实现 但是我想用布尔值实现
for sk in car_nm:
    if 'ak' in car_nm:
        print("对的")
        break
    else:
        print("w")
        break


cbd = ["11", "13", "24"]
for eat in cbd:
    if eat != True:
        print("丢了")
        break
    else:
        print("找回了")
        break
print("麻烦")

#进行对比 看看是够相等  相等就是Ture  不相等就是false


cbs = ["15", "20", "35"]
for thomas in cbs:
    if thomas[0] != True:
        print("托马斯")
        break
    elif thomas [1] != True:
        print("罗宾逊")
        break
    else:
        print("it")
print("你说谁")


#https://jiasuqi.xyz/static/webVPN_offline_install_manual.html
#谷歌浏览器 离线安装vpn

agetime = 10
if agetime < 9:
    print("幼儿园")
elif agetime >= 10:
    print("小学僧")
elif agetime >= 20:
    print("大学生")
else:
    print("判断不出来")


nd_dd = ["peper", "milk", "mush"]
if 'peper' in nd_dd:
    print("add peper")
if 'milk' in nd_dd:
    print("add milk")
if 'mush' in nd_dd:
    print("add mush")
print("\nFinished you pizza")

#第五章 小结
alien_coler = ["green", "yellow", "blue"]
if 'green' in alien_coler:
    print("这是个绿色的怪物，获得5分")
#第二个版本

alien_coler = ["yellow", "blue", "green"]
for i in alien_coler:
    if  'green' == False:                      #输出结果为空
        print("不包括蓝色")

alien_c = ["green", "blue"]
if 'green' in alien_c:
    print("玩家射杀外星人，获得5个点")
if alien_c[1] != 'green':
    print("玩家射杀的不是绿色的，获得10个点")



alien_c = ["green", "blue"]
if alien_c[1] == 'green':
    print("玩家射杀外星人，获得5个点")
elif alien_c[1] != 'green':
    print("玩家射杀外星人，是蓝色的")
else:
    print("玩家射杀的不是绿色的，获得10个点")


age_xz = 25
if age_xz < 2:
    print("婴儿")
elif 2 <= age_xz <= 4:
    print("步履蹒跚")
elif 4 < age_xz < 13:
    print("儿童")
elif 13 <= age_xz < 20:
    print("青少年")
elif 20 <= age_xz <65:
    print("成年人")
elif age_xz >= 65:
    print("老年人")


fa_fr = ["apple", "juice", "banana", "orange","ice"]
if 'apple' in fa_fr:
    print("add apple")
if 'juice' in fa_fr:
    print("add juice")
if 'banana' in fa_fr:
    print("add banana")
if 'orange'in fa_fr:
    print("add orange")
if 'ice' in fa_fr:
    print("add ice")
if 'milk' in fa_fr:
    print("add milk")
print("your favrite fruit is: ")


langue = ["c", "java", "c++","c", "python", "c"]
for a in langue:
    if a != 'c':
        print(a)


doc = ["1", "3", "7", "1", "2", "27", "1", "5"]
for dc in doc:
    if dc != '1':
    print(dc)



for x in range(20):
    for y in range(30):
        for z in range(40):
            if (x + y + z) == 100 and (x*5 + y*3 + z*3) == 100 and z%3 == 0:
                print(x,y.z)


money = 1000
card_no = int(input("请输入银行卡号"))
i = 0
if card_no == int(111111):
    print("卡号正确")
    #验证银行卡密码
    password = int(input("请输入密码"))
    while password != int('123456'):
        if i < 3:
            print("密码错误第%s次" % (i+1))
            pwssword = int(input("请重新输入密码"))
            i = i+1
        elif i == 3:
            print("密码错误6次请到柜台办理")
            break
    else:
        #验证输入金额是否大于余额
        qu_money = int(input("请输入取款金额"))
        while qu_money > money:
            print("您的余额不足，当前余额为: %s" %(money))
            qu_money = int(input("请重新输入取款金额"))
        else:
            money = money - qu_money
            print("取钱成功，您的余额为%s" %(money))
else:
    print("银行卡号错误")


xy_id = int(input("输入游戏id"))
i = 0
if xy_id == int('789123'):
    print("账号正确")
    password = int(input("输入密码"))
    while password != int('272727'):
        if i < 3:
            print("密码错误第%s次" % (i+1))
            password = int(input("请重新输入密码"))
            i = i+1
        elif i == 3:
            print("机会已用尽")
            print("请联系客服处理")
            break
        else:
            print("账号或密码错误")

else:
    print("抱歉，账号已注册或密码有误")


#五子棋源码
from graphics import *
from math import *
def gobangwin():
    win=GraphWin("this is a gobang game",400,400) #ÖÆ×÷21x21µÄÆåÅÌ
    win.setBackground("yellow")
    i1=0

    while i1<401:
        l=Line(Point(i1,0),Point(i1,400))
        l.draw(win)
        i1=i1+20
    i2=0

    while i2<401:
        l=Line(Point(0,i2),Point(400,i2))
        l.draw(win)
        i2=i2+20
    return win

def main():
    win = gobangwin()

    list1 = []
    list2 = []
    list3 = []

    change = 0
    g = 0
    m=0
    n=0

    while g == 0:

       if change%2 == 1:
        p1 = win.getMouse()
        if not ((round((p1.getX()+10)/20),round((p1.getY()+10)/20)) in list3):

             a1 = round((p1.getX()+10)/20)
             b1 = round((p1.getY()+10)/20)
             list1.append((a1,b1))
             list3.append((a1,b1))

             piece = Circle(Point(20*a1,20*b1),8) #´´½¨Æå×Ó
             piece.setFill('white')
             piece.draw(win)
             for m in range(21): #ÅÐ¶ÏÊäÓ®
                 for n in range(21):

                         if n<17 and (m,n) in list1 and (m,n+1) in list1 and (m,n+2) in list1 and (m,n+3) in list1 and (m,n+4) in list1 :
                             message = Text(Point(100,100),"white win.")
                             message.draw(win)
                             g = 1     #ÅÐ¶Ï°×ÆåÊúÐÐ
                         elif m<17 and  (m,n) in list1 and (m+1,n) in list1 and (m+2,n) in list1 and (m+3,n) in list1 and (m+4,n) in list1 :
                             message = Text(Point(100,100),"white win.")
                             message.draw(win)
                             g = 1   #ÅÐ¶Ï°×ÆåºáÐÐ
                         elif m<17 and n<17 and (m,n) in list1 and (m+1,n+1) in list1 and (m+2,n+2) in list1 and (m+3,n+3) in list1 and (m+4,n+4) in list1 :
                             message = Text(Point(100,100),"white win.")
                             message.draw(win)
                             g = 1    #ÅÐ¶Ï°×ÆåÐ±ÐÐ
                         elif m<17 and n>3 and (m,n) in list1 and (m+1,n-1) in list1 and (m+2,n-2) in list1 and (m+3,n-3) in list1 and (m+4,n-4) in list1 :
                             message = Text(Point(100,100),"white win.")
                             message.draw(win)
                             g = 1     #ÅÐ¶Ï°×ÆåÐ±ÐÐ
                         else: change = change+1  #»»ºÚÆå×ß

       else:
        p2 = win.getMouse()
        if not ((round((p2.getX()+10)/20),round((p2.getY()+10)/20)) in list3):

               a2 = round((p2.getX()+10)/20)
               b2 = round((p2.getY()+10)/20)
               list2.append((a2,b2))
               list3.append((a2,b2))

               piece = Circle(Point(20*a2,20*b2),8)
               piece.setFill('black')
               piece.draw(win)
               for m in range(21):
                 for n in range(21):

                         if n<17 and (m,n) in list2 and (m,n+1) in list2 and (m,n+2) in list2 and (m,n+3) in list2 and (m,n+4) in list2 :
                             message = Text(Point(100,100),"black win.")
                             message.draw(win)
                             g = 1    #ÅÐ¶ÏºÚÆåÊúÐÐ
                         elif m<17 and  (m,n) in list2 and (m+1,n) in list2 and (m+2,n) in list2 and (m+3,n) in list2 and (m+4,n) in list2 :
                             message = Text(Point(100,100),"black win.")
                             message.draw(win)
                             g = 1  #ÅÐ¶ÏºÚÆåºáÐÐ
                         elif m<17 and n<17 and (m,n) in list2 and (m+1,n+1) in list2 and (m+2,n+2) in list2 and (m+3,n+3) in list2 and (m+4,n+4) in list2 :
                             message = Text(Point(100,100),"black win.")
                             message.draw(win)
                             g = 1   #ÅÐ¶ÏºÚÆåÐ±ÐÐ
                         elif m<17 and n>3 and (m,n) in list2 and (m+1,n-1) in list2 and (m+2,n-2) in list2 and (m+3,n-3) in list2 and (m+4,n-4) in list2 :
                             message = Text(Point(100,100),"black win.")
                             message.draw(win)
                             g = 1   #ÅÐ¶ÏºÚÆåÐ±ÐÐ
                         else: change = change+1  #»»°×Æå×ß

    message = Text(Point(100,120),"Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()

main()

#批量下载文件源码

from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool
import requests
import sys
import os

def download(url):
    chrome = 'Mozilla/5.0 (X11; Linux i86_64) AppleWebKit/537.36 ' + \
        '(KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    headers = {'User-Agent': chrome}
    filename = url.split('/')[-1].strip()
    r = requests.get(url.strip(), headers=headers, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    print filename, "is ok"

def removeLine(key, filename):
    os.system('sed -i /%s/d %s' % (key, filename))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        f = open(filename, "r")
        p = Pool(4)
        for line in f.readlines():
            if line:
                p.spawn(download, line.strip())
                key = line.split('/')[-1].strip()
                removeLine(key, filename)
        f.close()
        p.join()
    else:
        print 'Usage: python %s urls.txt' % sys.argv[0]

# py获取系统信息源码
import os,inspect,socket,time,pymysql
num = 0
class Mysql:
    def __init__(self,host,user,password,db):
        self.cnn = pymysql.connect(host=host,user=user, passwd=password, db=db, charset='utf8')
        self.cur= self.cnn.cursor()

    def run(self,sql):
        self.cur.execute(sql)

    def cmd(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def commit(self):
        self.cnn.commit()

    def close(self):
        self.cur.close()
        self.cnn.close()

class mon:
    def __init__(self):
        self.db_file='./db.json'
        self.data={}

    def getAmber(self):
        global num
        num+=1
        return num

    def getDate(self):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

    def getProcess(self):
        return os.popen('ps -ef |wc -l').readlines()[0].split()[0]

    def getDisk(self):
        return os.popen("df -m |grep '/$'").readlines()[0].split()

    def getMem(self):
        return os.popen('free -m').readlines()[1].split()[1:4]

    def getSwap(self):
        return os.popen('free -m').readlines()[3].split()[1:]

    def getLoad(self):
        return os.popen('uptime').readlines()[0].split()[-3:]

    def getHost(self):
        return socket.gethostname()

    def getUser(self):
        return os.popen('uptime').readlines()[0].split()[3]

    def getRuntime(self):
        return os.popen('uptime').readlines()[0].split()[2]

    def getSystem(self):
        return os.popen('cat /etc/redhat-release').readlines()[0].split('\n')[0]

    def getKerner(self):
        return os.popen('uname -r').readlines()[0].split('\n')[0]

    def run(self):
        for fun in inspect.getmembers(self,predicate=inspect.ismethod):
            if fun[0][:3] == 'get':
                #print fun[1]()
                self.data[fun[0][3:]] = fun[1]()
        #print self.data
        return self.data
        #file(self.db_file,'a').write("%s\n" % self.data)
        time.sleep(15)
if __name__ == "__main__":
    mysql=Mysql('192.168.0.58','root','123456','host')
    while 1:
        res= mon().run()
        memTotal=int(res['Mem'][0])
        diskTotal=int(res['Disk'][0])
        memFree=int(res['Mem'][2])
        diskFree=int(res['Disk'][2])
        cpuPercent=int(res['Process'])
        ip=os.popen("ifconfig |grep  'Bcast' |awk -F: '{print $2}'").readlines()[0].split()[0]
        print('-------------------',ip)
        ress=mysql.cmd('select * from hostinfo where ip="%s"'%ip)
        ress=list(ress[0])
        for i in ress[3:]:
            lists=eval(i)
            print(lists)
            lists['data'].pop(0)
            lists['data'].append(eval(lists['name']))
            sqls='update hostinfo set %s = "%s" where ip="%s"'%(str(lists['name']),lists,ip)
            mysql.cmd(sqls)
        mysql.commit()
        print('------------------------------------------------')
        time.sleep(30)

#生成随机手机号
import random                                        #声明random
for _ in range(5):                                   #想打印几个手机号 就把5改成几
    sjh = ["132", "133", "134", "135", "136", "137", "138", "139"]  #设置手机号前三位的随机数字
    str = random.choice(sjh)+"".join(random.choice("0123456789") for _ in range(8))
    print(str)

import random
for xh in range(4):
    sjh = ["151", "188", "177", "189", "156"]
    str = random.choice(sjh)+"".join(random.choice("56789")for _ in range(8))
    print(str)

#生成随机身份证号
import random
for _ in range(3):
    sfzh = ["110","120","223"]
    str = random.choice(sfzh)+"".join(random.choice("0123456789x")for _ in range(15))
    print(str)

cailiao = ["柿子", "苹果", "香蕉", "红葡萄", "黑葡萄", "猕猴桃"]
for zuo in cailiao:
    if cailiao == '核桃':
        print("抱歉，这种材料用完了")
        break
    else:
        print("adding" + zuo +".")
print("\n 谢谢品尝")

#字典
zi_d = {"dalas":33, "lal":99,
         "dudu":56, "lac":47,
          "ny":66, "gl":89
       }
for qiu in zi_d:
    if 'dules' in zi_d:
        print("go")
        break
    else:
        print("没毛病")
        break
#字典的键和值
fa_la = {'python': 'jin', 'java': 'ruby', 'edware': 'python'}
for name, language in fa_la.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

#求平均分
d_cj = {'adam': 95, 'das':85, 'wang':59, 'paul':74}
sum = 0
for key, value in d_cj.items():
    sum = sum + value
    print(key, ':', value)
print("平均分:", sum /len(d_cj))


fa_la = {'python': 'jin', 'java': 'ruby', 'edware': 'python'}
lo = ["jin", "java"]
for name in fa_la.keys():
    print(name.title())

    if name in lo:        #fa_la() not in
        print("Hi "  + name.title() + " I see you is: "  +fa_la[name].title())
    else:
        print("sorry I do't know " +name.title())


#title()
str = ' the worldwide web '
str.title()                   #每个单词的首字母大写
str.title().strip()           #strip()函数把首尾的空格去掉

#对包含重复的列表调用set()函数 去掉重复
fa_la = {'11': 'jin', '12': 'ruby', '13': 'python', '22':'java', '27':'java'}
for langue in set(fa_la.values()):
    print(langue.title())

aone = {"外星人":1, "外星人2号":2}
asec = {"火星人":3, "火星人2号":4}
athr = {"水星人":5, "水星人2号":6}

aline = [aone, asec, athr]
for alins in aline[:2]:               #[:2]取前两个
    print(alins)

aone = {"外星人":1, "theee":['first', 'second']}
for theee in aone['theee']:
    print(theee)

la_la = {'nams': ['py', 'java'],
         'namo': ['ruby', 'c'],
         'namt': ['py', 'java', 'c']}
for name,langue in la_la.items():
    print('\n' +name.title() +" is the right")
    for langue in languages:
        print('\t' + langue.title())

fav_lau = {'fir':['py','ruby'],
           'two':['java', 'c'],
           'thr':['c', 'java', 'py']}
for name,languages in fav_lau.items():              #两个循环
    print('\n' + name.title() + " is the best answer" )
    for language in languages:
        print('\t' + language.title())

uesr = {"james":
       {'first':'leborn',
        'second':'james',
        'addr':'twotimes'},
        "ivrson":
        {'first':'alen',
         'second':'iveson',
         'addr':'fourtimes'}
        }
for username,user_info in uesr.items():   #第一个字典的键存到username变量中 将键对应的值存到user_info中
    print("\nUsername:" + username)
    full_addr = user_info['first'] + "" + user_info['second']  #将第二个字典的两个键和对应的值相加
    address = user_info['addr'] + "" + user_info['addr']       #将第二个字典的最后一个键和对应的值打印出来

    print("\tFull name: " + full_addr.title())
    print("\taddr: " + address.title())



#input()
message = input("tell me why , and I'll fucking you")
print(message)

name = input("Please Enter your name: ")
print("Hello, " + name + " !")

portpp = "if you tell me who you are I'll told you farher is"
portpp += "\n and who is you mather"
cd = input(portpp)

# -*- coding : utf-8 -*-
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()