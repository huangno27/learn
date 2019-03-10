
#coding = utf-8
proverb = "A penny saved"
proverb = proverb + "is a penny eraned"
print(proverb)                                       #元素的添加
proverb_saved = 0
proverb_saved = proverb_saved + 1
print(proverb_saved)

a = ("first", "second", "third")
print("the first element of the tuple is %s" % a[0])  #位置从0开始 读取0位置的元素
a = ("5", "16", "27")
print("hello world is %s" % a[2] )                    #位置从0开始 读取2位置的元素
print(a[len(a) - 1])                                  #len是内置函数 从1开始读取位置 所以会有 - 1
a = ["0", "1", "2", "4", "7"]
print(a[len(a) - 1])                                  #统计元组里元素的个数
b = (a, "bitch is a girl")
print(b)                                              #嵌套元组，元组中的一个元素也可以是对另外一个元组的引用
a = ("1", "2", "5")
b = (a, "bitch is a bitch")
print("$s" %b[0])                                      #位置从0开始读取
print("%s" %b[0] [0])                                  #读取a元组中的0号位置元素
zaofan = ["tea", "coffee", "rich"]                     #列表是用方括号
count = 0
print("today is breakfast is %s" % zaofan[count])      #count = 0 手动加1 读取下一元素
zaofan[count] = "sausages"                             #列表可以修改元素
print("today is breakfasr is %s" % zaofan[count])
zaofan.append("waffles")                               #向列表里添加新元素 append方法只能添加一个元素
count = 4
print("today is breakfast is %s" % zaofan[count])      #检验新增加的新元素
zaofan.extend(["juice", "egg", "decaf", "oatmeal", "milk"])
print(zaofan)                                          #extend方法可以添加多个新元素到列表
print(zaofan[len(zaofan) - 1])                         #len函数计算出 位置上的元素是啥
print(len(zaofan))                                     #len函数结算处 列表的长度
{}                                                     #字典花括号表示
menus_specials = {}
menus_specials["zaofan"] = "canadian ham"
menus_specials["lunch"] = "tuna surprise"
menus_specials["dinner"] = "cheesrburger Deluxe"
menus_specials = {"breakfast";"egg and milk"}
print(menus_specials)                                   #打印字典内
print(menus_specials["breakfast"])                      #打印早餐（键）对应的实物（值）
menus_specials = {"breakfast";"2 hot dog",..."lunch";"rich",..."dinner";"egg"}
print(menus_specials[b l d ])                           #打印时输入对应的键才能打印对应的值
print(menus_specials)
menus_specials = {"breakfast":"egg","lunch":"rich","dinner":"2 hot dogs"}
print("%s" % menus_specials["breakfast"])
print ("%s" % menus_specials["lunch"])
print("%s" % menus_specials["dinner"])                   #如果键是字符串需要加引号，如果键是数值仅使用数值就可以
hungry=menus_specials.keys()
print(list(hungry))                                      #keys方法要求字典以视图的方式返回所有值，以便用户查找键
starving=menus_specials.value()
print(list(starving))                                    #value方法要求以视图形式返回所有的值
#值可以相同，但是键不能相同
last_name = ["doglass","james","kobe","ingram"]          #分片
print("%s" % last_name[0])
print("%s" % last_name[0][0])
print("$s" % last_name[-1])                              #-1 代表从后往前读取 -1是倒数第一个 -2是倒数第二个
#习题
m = ("12", "10", "2009")
print("this milk will on %s" % '/'.join(m))               #打印格式
milk_carton = {"expiration_data":"10/09/2009","cost":"50.00","fl_oz":"41.00"}
dlist = list(milk_carton.keys())
print(dlist)                                               #只打印字典中键对应的值
if 'age' in a.keys():
    print a['age']                                         #如果不确定这个键在字典内
