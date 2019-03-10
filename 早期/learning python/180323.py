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


