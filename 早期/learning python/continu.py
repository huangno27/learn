
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


