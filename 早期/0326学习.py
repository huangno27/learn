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

name = input("Please Enter your name: ")    #input()需要清晰易懂的指出你希望用户提供什么样的信息时
print("Hello, " + name + " !")

portpp = "if you tell me who you are I'll told you farher is"
portpp += "\n and who is you mather"
cd = input(portpp)

name = input("what 's your name : ")
print("Hello " + name + "!")
age = input("How old are you ? ")
print("Yeah " + age + " Too young")
where = input(name + " Where are you from ?")
print("oh " + where + " so beautiful")


age = input(" How old are you ? ")
#  接 age = in(age) 将输入的字符串转换为数值

jiage = input(" How much ?")
jiage = int(jiage)
if jiage <= 15:
    print("Get it")
else:
    print("so")

jiage = int(input("how many"))
if jiage <= 10:
    print("get it")
else:
    print("no money")

#求模运算符 %  只返回余数 整除返回0
jiage = int(input("how many"))
if jiage % 2 == 0:
    print("这是个偶数")
else:
    print("这是个奇数")

propmt = " tell me would you like go on ?"
propmt += "\nEnter 'quit' to end the game."
message = ""
while message != 'quit':
    message = input(propmt)
    if message != 'quir':                    #加上if语句 将不会再把输入的值再下一行重新打印一次
    print(message)
    print("see you again")


#标志  要求很多条件都满足时才继续运行程序，可以定义一个变量，用于判断整个程序是否处于活动状态中 这个变量被称为标志

propmt = " tell me would you like go on ?"
propmt += "\nEnter 'quit' to end the game."
active = True                                     #标志 为  active
while active:
    message = input(propmt)
    if message == 'quit':
        active =  False
        print("Game Over !")                     #elif 添加更多条件

    else:
        print(message)

propmt = " tell me would you like go on ?"
propmt += "\nEnter 'quit' to end the game."
while True:                                      #while True的循环会一直循环知道碰到 break条件才会终止
    dinns = input(propmt)
    if message == 'quit':
        active =  False
        print("Game Over !")
        break
    else:
        print(dinns)


people_num = 0                        #先设置成0
while people_num < 10:
    people_num += 1                    #设置步长为1
    if people_num % 2 == 0:            #当循环的值 整除 2  = 0 时 跳过这个继续循环
        continue
    else:
        print(people_num)


#首先创建一个待验证的列表
#和一个已经用过验证的列表
wyz_user = ["alice", "menta", "davic", "arde"]
yyz_user = ["alinas"]
#验证每个用户，知道没有待验证为止
#将每个验证过的添加到已验证列表
while wyz_user:
    tgyz_user = wyz_user.pop()           #.pop()是从列表中倒序删除元素 存储到通过验证列表

    print("Verifying user: " + tgyz_user.title())
    yyz_user.append(tgyz_user)
#显示所有已验证用户
print("\n the floowing user have been 已验证: " )
for kd in yyz_user:                      #最后循环已验证的列表，打印出来核对
    print(kd.title())


cflb = ["cat", "dog", "fish", "cat", "pig", "mouse", "cat"]
print(cflb)
while 'cat' in cflb:
    cflb.remove('cat')                  #remove()删除特定元素，继续循环继续删除 直到删除干净为止
    if 'cat' not in cflb:
    print(cflb)

# 使用用户输入来填充字典
resports = {}
#设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 输入被调查者的名字和回答
    name = input("\n What 's your name ? ")
    resport = input("Which color is you like ? ")
    #将答卷存在字典中
    resports[name] = resport
    #看看是否还有人要参加问答
    repeat = input("Would you like to let other person ask ?(yes/no)")
    if repeat == 'no':
        polling_active = False
#调查结果，显示结果
print("\n - - - Poll Result - - -")
for name,resport in resports.items():
    print(name + " would you like to climb " + resport + ".")


zi_di = {}                                                #空字典
zt_on = True                                              #设置标志
while zt_on:                                              # 字典进入循环
    name = input("\n What 's your name ?")
    hobby = input("which color do you liake ?")
    zi_di[name] = hobby                                   #存储字典的键=值
    again = input("do you like ask other people ? (yes/no)")
    if again == 'no':                                      #if 语句设置状态为 False
        zt_on = False
for name,hobby in zi_di.items():                           #最后循环键和值
    print(name + " Thank you Baby !!" + hobby + ".")


sa_or = ["ab", "ac", "ad", "af", "ae"]
fi_or = []
for chi_s in sa_or:
    if 'ab' in chi_s:
        print("这是ab")
    elif 'ac' in chi_s:
        print("这是ac")
    elif 'ad' in chi_s:
        print("这是ad")
    elif 'af' in chi_s:
        print("这是af")
    elif 'ae' in chi_s:
        print("这是ae")
    else:
         break
print(chi_s)

fi_or = chi_s
print(fi_or)

sa_or = ["ab", "ac", "ad", "af", "ae"]
fi_or = []
while sa_or:
    se_or = sa_or.pop()
    print(se_or.title())
    fi_or.append(se_or)
for kd in fi_or:
    print(kd)




# -*-coding:utf-8-*-
from selenium import webdriver
import unittest
import time

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com/")
        self.driver.maximize_window()
        time.sleep(2)
        self.xinlang=self.driver.find_element_by_xpath(".//*[@id='site-my-list']/ul/li[2]/a")
        time.sleep(2)
        self.xinlang.click()



    def tearDown(self):
        self.driver.quit()




    def test_baidu(self):
        all_h = self.driver.window_handles
        self.driver.switch_to.window(all_h[1])
        time.sleep(2)
        self.title = self.driver.title
        time.sleep(2)
        self.assertEqual(self.title,u"新浪首页")

# -*-coding=utf-8-*-
import HTMLTestRunner
import unittest
import danyuan.baidu


suit =unittest.TestSuite()
suit.addTest(unittest.makeSuite(danyuan.baidu.Baidu))
filename=r"C:\Users\13436\Desktop\case.html"
filen = file(filename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=filen,title=u"百度一下",description=u"测试用例")
runner.run(suit)

Pi = 2.2
def main():
    print("Pi: ", Pi)
main()

Pi = 2.2
def main():
    print("Pi :", Pi)
if __name__ == "__main__":
    main()








# -*-coding=utf-8-*-
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()



public class aa
{
public int staue;
public String message;
public String username;
}
需要继承HttpServlet
public class Login extends HttpServlet
{
 @Override
protected void doGet(HttpServletRequest req, HttpServletResponse resp)
		throws ServletException, IOException
		{
设置编码格式
	//指定接收和输出的编码格式为utf-8
			//接受的编码格式为utf-8		
			req.setCharacterEncoding("UTF-8");
			//返回的编码格式为utf-8		
			resp.setCharacterEncoding("UTF-8");

	 String userString = req.getParameter("username");
	 String password = req.getParameter("password");
	 System.out.println("用户名"+userString+","+"密码"+password);
	 实例化对象
	 aa a = new aa();
	 a.staue=1;
	 a.username = userString;
	 a.message="成功";
      转为json数据 序列化
	 String json = new Gson().toJson(a);
然后通过流写进去
	 PrintWriter writer=resp.getWriter();
	 writer.write(json);
		writer.flush();
		writer.close()
  }


def greet_user(username):             #形参
    """显示简单的问候语"""
    print("Hello! " + username.title() + " welcome to python")

greet_user('杰西卡')                  #实参
greet_user('奥尼尔')
greet_user('迪奥')

def des_pet(animal_type, pet_name):                   #animal_typr='amao'  des_pet会得到默认值为amao与其对应起来
    """显示宠物信息"""
    print("\n I  have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name)

des_pet(animal_type='waker', pet_name='bidi')           #实参可以直接给值，确认键和值存到一起传参准确，
des_pet('hamster', 'castom')
des_pet('monkey', 'james')


def des_pet(pet_name, animal_type='ao'):
    print("\n I have a " + animal_type)
    print("My" + animal_type + "'s name is " + pet_name)

des_pet(pet_name='biu')
des_pet(animal_type='duke', pet_name='ding')

def get_for_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + '.' + last_name
    return full_name.title()
musician = get_for_name('jimi', 'batler')
print(musician)



def name_qm(f_name,s_name):
    full_name = f_name + s_name
    return full_name.title()
xingxing = name_qm('ran','xingxing')
print(xingxing)
daxing = name_qm('huang','huang')
print(daxing)

#让实参变成可选的
def name_qum(x_name, la_name, mi_name=''):
    if mi_name:
        full_name = x_name + '' + mi_name + '' + la_name
    else:
        full_name = x_name + la_name
    return full_name.title()
chine = name_qum('张三','李四', '和')
chind = name_qum('赵', '钱孙')

#引用字典
def you_name(dt_name,last_name):
    person = {'first':dt_name, 'last':last_name}
    return person
chine = you_name('alan', 'waker')
print(chine)

def coco_name(cz_ming,dz_ming):
    zuo = {'first':cz_ming, 'last':dz_ming}
    return zuo
name = coco_name('ji','mao')
print(name)

def cos_name(b_k,d_j,age=''):
    kt_sk = {'first':b_k, 'last':d_j}
    if age:
        kt_sk['age'] = age
    return kt_sk
bo = cos_name('ha','ma',age=27)
print(bo)


#coding:utf-8
def get_for_name(bz_name,ck_name):
    quan_name = bz_name + '' + ck_name
    return quan_name.title()
# 这是一个无限while循环
while True:
    print("\n please tell me you name: ")
    print("(Enter 'q' at anytime to quit)")
    b_name = input("Bz_name:")
    if b_name == 'q':
        break
    c_name = input("Ck_name:")
    if c_name == 'q':
        break
    for_name = get_for_name(b_name,c_name)
    print("\nHello, "+ for_name + "!")

def city_country(stanito,chile):
    ci_co = {"hongkong":china, "losangel":USA,"moerben":aostrulia}
    return ci_co
ci_co = city_country()
print(ci_co)

def city_country(city_s = "Santiago",city_m="Chile"):
    di_n = city_s + city_m
    return di_n.title()

cheng_s = city_country(city_s='losangel',city_m='usa')
print(cheng_s)
cheng_d = city_country(city_s='haerbin',city_m='china')
print(cheng_d)
cheng_f = city_country(city_s='moerben',city_m='aosichuiliya')
print(cheng_f)


def zh_j(gs_n,zj_n,much=''):
    shang_dian = {"歌手":gs_n,"专辑名":zj_n,}
    if much:
        shang_dian['much'] = much
        return shang_dian
bo_o = zh_j('jay','jaychou',much=22)
print(bo_o)
po_o = zh_j('ck','dj',much=10)
print(po_o)
mo_o = zh_j('wang','first love',much=11)
print(mo_o)

def g_zj_q(g_n,zj_m,s_l=''):
    chao_shi = {"歌手":g_n,"专辑":zj_m}
    if s_l:
        chao_shi['s_l'] = s_l
        return chao_shi
mo_m = g_zj_q('jack','do love', s_l=10)
print(mo_m)
mo_c = g_zj_q('bk', 'dalaiwen',s_l=9)
print(mo_c)

def greet_user(names):
    for name in names:
        msg = "Hello " + name.title() + " !"
        print(msg)
usernames = ['lady','rudy','mickel','jackson']
greet_user(usernames)



def g_shock(names):
    for name in names:
        bk = "Hi Mr" +name.title() + " !"
        print(bk)
ddname = ['xiaobai','xiaohei','biubiu','piupiu']
g_shock(ddname)


def g_shocl(muchs):
    for much in muchs:
        dfj = "Hey men " + much.title() + "!"
        print(dfj)

ddmuch = ['a', "张飞", "李逵","studio"]
g_shocl(ddmuch)

#在函数中修改列表
#先创建一个空列表，其中包含一些要打印的设计
unprinted_designs = ['ipone','android','nokia']
completed_models = []
#模拟打印每个设计，直到没有未打印的设计为止
#打印每个设计后 都将其移到列表completed_models中
while unprinted_designs:
    curren_design = unprinted_designs.pop()
    #模拟根据设计制作3D打印模型的过程
    print("Printing model: " + curren_design)
    completed_models.append(curren_design)

#显示打印好的所有模型
print("\n The following models have been printed: ")
for c_mm in completed_models:
    print(c_mm)

one_biao = ['laker','losangel','kobe']
two_biao = []
while one_biao:
    three_biao = one_biao.pop()
    print("This is " + three_biao)
    two_biao.append(three_biao)
for ball in two_biao:
    print(" Everybody want to look:" + ball)

one_biao = ['losangel','laker','kobe']
two_biao = []
while one_biao:
    two_biao = one_biao.pop()
    print("直接让他等于")



def print_model(biao_yi,biao_zi):
    while biao_yi:
        biao_san = biao_yi[ : ]       #切片  将biao_yi的副本传给参数，继续保存列表中的数据
        print(biao_san)
        print("验证biao_yi的数据还在列表中 对biao_yi进行打印")
        print(biao_yi)
        biao_zi.append(biao_san)
        print(biao_zi)
        break
def show_com_model(biao_zi):
    print("显示打印好的所有模型:")
    for dayin in biao_zi:
        print(dayin)
biao_yi = ['ipone','nokia','android','seyban']
biao_zi = []
print_model(biao_yi,biao_zi)
show_com_model(biao_zi)

def show_magicmans(dlss):
    for ak in dlss:
        msg = ak.title()
        print(msg)

Magic = ['mss','jbr','kb','kd']
show_magicmans(Magic)


def smz_cl(*calling):
    print("\n 顾客想要:")
    print(calling)

smz_cl('rou')
smz_cl('cai')
smz_cl('tomato')

def jian_jie(xing_o,ming_o,**ziliao):
    zidian = {}
    zidian['xing'] = xing_o
    zidian['ming'] = ming_o
    for key,value in ziliao.items():
        zidian[key] = value
    return zidian
wo_de = jian_jie('huang','yue',add='beijing',hobby='play',wan='piqiu')
print(wo_de)

def make_car(subrru_o,outback_o,**car_info):
    car_id = {}
    car_id['name'] = subrru_o
    car_id['color'] = outback_o
    for key,value in car_info.items():
        car_id[key] = value
    return car_id
new_car = make_car('subaru','outback',yanse='blue',two_package='True')
print(new_car)

#导入模块的方法 import 模块名.函数名（数据）
#导入模块中的特定函数方法 from moudle_name import function_name
#导入模块中任意数量的函数 from moudle_name import function_0,function_1（用逗号分隔函数名）
#导入只想使用的函数  import 模块名.函数名（）
#如果函数名字过长或冲突时 可以给函数起别名（外号） from 模块名 import 函数名 as 新名字
from pizza import make_pizza as mp
mp(16,'apple')
mp(12,'red','black','blue')
#给模块指定别名 如模块pizza指定别名为p
import pizza as p
p.make_pizza(16,'apple')
#导入模块中的所有函数 from pizza import * 使用*可以导入所有函数
#一般不可取 遇到别人写的模块时 导入所有函数 会引起冲突 函数或变量名会被覆盖 进而覆盖函数

#函数的编写
#给形参指定默认值时 等号两边不要有空格
def function_name(function_0,function_1='等号两边不要有空格'):
# 对于函数中调用中的关键字实参 也要遵循上面的规定 不要有等号
# 如果实参的长度太长时 可在函数定义中输入左括号后回车 并在下一行按两次tab键 从而缩进到一层的函数体
def function_name(
        part_0,part_1,part_2,
        part_11,part_12,part_13):


# 类
class Dog():   #创建类 类的首字母必须大写  （）为空是要从空白处创建这个类
    """一次模拟小狗的简单测试"""
    def __init__(self,name,age):  #将特殊方法定义成包含三个形参 self必不可少 还必须位于其他形参前面
        """初始化属性name和age"""
        self.name = name    #变量都有前缀self 可提供类中的所有方法使用
        self.age = age      #获取存在形参name和age中的值 并将值存储到变量 name和age中，然后变量被关联到当前的实例
                            #像这样通过实例访问的变量称为属性

    def sit(self):          #定义方法 不需要额外的信息 只有一个形参self 后面将创建的实例能够访问这些方法
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + "is now sitting.")

     def roll_over(self):   #当前只是打印一条消息 指出小狗正蹲下或打滚 但可以拓展这些方法模拟实际情况
         """模拟小狗被命令时打滚"""
         print(self.name.title() + "rolled over")

#根据类创建实例
#class Dog():
my_dog = Dog('weili',6)
#先创建一行名为weili和6的小狗 遇到这行代码 将用实参调用Dog类中的_init_（）方法 创建一个特定小狗的实例
#并使用我们提供的值来设置属性name 和 age
#类的方法并未显式的包含return语句 但py自动返回一个表示这条小狗的实例 将实例存储在变量my_dog中
#默认大写字母开头是类 小写字母的名称指的是根据类创建的实例

print("My dog's name is "+ my_dog.name.title() + ".")
#句点表示法my_dog.name 先找实例my_dog再查找与这个实例相关联的属性
#第一条print中my_dog.name.title()将my_dog的属性name的值'weili'改成为首字母大写
print("My dog is " + str(my_dog.age) + " years old.")
#第二条print中my_dog.age.title()将my_dog的属性age的值'6'改成为字符串
#输出是有关my_dog的摘要

class Resrant():
    def __init__(self,resranr_name,resrant_typeo):
        self.resrant_name = resranr_name
        self.resrant_typeo = resrant_typeo

    def desc_resrant(self):
        print(self.desc_resrant() + "餐厅正在营业中")

    def open_resrant(self):
        print(self.open_resrant() + "餐厅正在营业中")

my_resrant = Resrant('seveneleven',11)
print("My restrurant is " + my_resrant.resrant_name.title() + " .")
print("My restrurant " + str(my_resrant.resrant_typeo) + " is working !")

your_resrant = Resrant('huanlian',9)
print("The " + your_resrant.resrant_name.title() + " is your")

class Rubd():
def _init_(self,属性1，属性2):
self.属性1 = 属性1
self.属性2 = 属性2
def fangfa(self):
print()
def fangfa2(self)
print()
 ruby = Ruby(属性值1，属性值2)
 print( ruby.属性3.title())
 ruby.fangfa()
 ruby.fangfa1()
 rub1= Ruby()
 rub2 = Ruby()




import sys

sys.setrecursionlimit(1000000) #例如这里设置为一百万


class User():
    def __init__(self,first_name,last_name,qt_sx):
        self.first_name = first_name
        self.last_name = last_name
        self.qt_sx = qt_sx

    def desc_user(self):
        print(self.desc_user()) #这里可以替换成return return self.desc_user
        print("你是一只猪")

    def greet_user(self):
        print(self.greet_user())

beer = User('rudi','kackson','american')
print(beer.first_name.title() +" " + beer.last_name + " " + beer.qt_sx)
beer.desc_user()
print(beer.desc_user)


#1.直接修改属性的值时  需要先设置新的属性值 新属性 = 任意数 这算作被读取的值 再添加读取这个值得方法 def方法名任意 打印读取到的 新属性 最后再调用读取这个值得方法





#类的继承  一个类继承另一个类时，新的类继承了原有类的所有属性和方法
#原有的类叫父类 新的类叫子类 子类继承了父类所有的属性和方法，同时还定义了自己的属性和方法












