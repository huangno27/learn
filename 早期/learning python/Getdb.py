import pymysql
import urllib.request
import ssl
import json
#import prettytable
from prettytable import PrettyTable

began = 'began'
def Find(place):
    db = pymysql.connect("localhost","root","lcw123456","location",charset='utf8')
    cusor = db.cursor()
    sql = "SELECT * FROM 12306place \
           WHERE place = '%s' " % place
    a = cusor.execute(sql)
    while a==0:
        checkplace = input("输入错误，请重新输入：")
        sql = "SELECT * FROM 12306place \
               WHERE place = '%s' " % checkplace
        a = cusor.execute(sql)
    results = cusor.fetchall()
    for i in results:
        fping = i[2]
    return fping

def Findp(ping):
    db = pymysql.connect("localhost", "root", "lcw123456", "location", charset='utf8')
    cusor = db.cursor()
    sql = "SELECT * FROM 12306place \
               WHERE ping = '%s' " % ping
    cusor.execute(sql)
    results = cusor.fetchall()
    for i in results:
        fping = i[1]
    return fping

def getHtml(url):
    headers = {
               'Accept': 'text/html,application/xhtml+xml,application/xml',
               'Accept - Encoding': 'gzip, deflate',
               'Accept - Language': 'en - US, en;q = 0.5',
               'User - Agent': 'Mozilla / 4.0(compatible;MSIE7.0;WindowsNT10.0;WOW64;Trident / 7.0;.NET4.0C;.NET4.0E;InfoPath.3)',
               'Referer':'https://kyfw.12306.cn/otn/leftTicket/init'
               }
    req = urllib.request.Request(url,headers=headers)
    gcontenxt = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    response = urllib.request.urlopen(req,context=gcontenxt)
    rep = json.loads(response.read())#.decode('utf-8')
    return rep

def T(t):
    if t == '':
        t = '_-'
    return t


#print(endp)
#startp = 'BXP'
#endp = 'PXG'
#Startptime = '30'

#print(tb)
#print("车次 出发站 到达站 出发时间 到达时间")
def message (get):
    global shanwu
    shanwu = []
    t = []
    tb = PrettyTable(["车次", "出发站", "到达站", "出发时间","到达时间","历时","乘车日期","商务座","特等座","一等座","二等座","高级软卧","软卧","硬卧","软座","硬座","无座","其他","状态"])
    tb.align["车次"] = "l"
    tb.padding_width = 1
    for i in get['data']['result']:
        t = i.split('|')[-3]#.split('\n')
        t = T(t)
        s = i.split('|')[-4]#.split('\n')
        s = T(s)
        k = i.split('|')[-5]#.split('\n')
        k = T(k)
        a = i.split('|')[-6]#.split('\n')
        a = T(a)
        b = i.split('|')[-7]#.split('\n')
        b = T(b)
        c = i.split('|')[-8]#.split('\n')
        c = T(c)
        d = i.split('|')[-9]#.split('\n')
        d = T(d)
        e = i.split('|')[-10]#.split('\n')
        e = T(e)
        f = i.split('|')[-11]#.split('\n')
        f = T(f)
        g = i.split('|')[-12]#.split('\n')
        g = T(g)
        h = i.split('|')[-13]#.split('\n')
        h = T(h)
        raw_id = i.split('|')[-32]
        raw_star = i.split('|')[-29]
        raw_star = Findp(raw_star)
        raw_end = i.split('|')[-28]
        raw_end = Findp(raw_end)
        raw_timebg =  i.split('|')[-27]
        raw_timeend = i.split('|')[-26]
        raw_timeuse = i.split('|')[-25]
        raw_timego = i.split('|')[-22]
        raw_state = i.split('|')[-34]
        #print(raw_state)
        tb.add_row([raw_id,raw_star,raw_end,raw_timebg,raw_timeend,raw_timeuse,raw_timego,t, e, s, k, c, g, b, f, a, d, h,raw_state])
        #tb.add_row(["---","---","---","---","---","---","---","---","---","---","---","---","---","---","---","---","---","---","---"])
        #print(raw_id,raw_star,raw_end,raw_timebg,raw_timeend,raw_timeuse,raw_timego,t, e, s, k, c, g, b, f, a, d, h,raw_state)
        #print(raw_timego)
    return tb
while began == 'began':
    Startplace = input("请输入始发站:")
    print(Startplace)
    if Startplace == 'exit':
        began = 'exit'
        break
    startp = Find(Startplace)
    Endplace = input("请输入到达站:")
    if Endplace == 'exit':
        began = 'exit'
        break
    endp = Find(Endplace)
    Startptime = input("请输入乘车日期（只需要输入日期入：06）:")
    if Startptime == 'exit':
        began = 'exit'
        break
    url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-05-%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT" % (
    Startptime, startp, endp)
    # print(url)
    get = getHtml(url)
    print(message(get))
    con = input("是否继续查询，若不继续请输入exit，若继续请按任意键:")
    if con == 'exit':
        began = 'exit'
        break
    #print(t,e,s,k,c,b,g,f,a,d,h)
print("查询完毕，谢谢！")