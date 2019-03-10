# %d 整数    %f 浮点数     %s 字符串     %x 十六进整数

zhanwei = 'Hi, %s you have $%d.' % ('michael',100)
print(zhanwei)

list = ['1', '2', '3']
list.append(0)          #添加元素到末尾
list.insert(1,'5')      #指定位置添加
print(len(list))        #统计列表里总共有多少元素
print(list)

list.pop()              #删除最后一位
list.pop(1)             #指定位置删除   1代表索引

list[1] = '27'          #替换元素的时候可以直接赋值给对应的索引位置


tuple                   #tuple初始化就不能修改


# input

birth = input('birthday: ')
if birth < 2000:
    print("00前")
else:
    print("80后")
#input输入1982 会报错 是因为input()返回的数据类型是str，str不能与整数直接比较
#必须先把str强制转换成整数， python提供了int()函数来完成这件事
s = input("birth: ")
birth = int(s)
if birth < 2000:
    print()
else:
    print()
#但是如果输入的是abc还是会报错，因为int()函数 发现一个字符串不是合法的数字时 会报错
#程序就会退出了 用调试 try expect 修改
birth = int(input("birth: "))

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n-2
print(sum)


# 赋值: l = [1, "hello", ("a", "b")]
# 获取: a = l[0] # 通过索引获取
# 增: l.append("c");l.extend(["d","e"]);l+["f"]
# 删: l.pop() # 按索引删除,无参数默认删除最后一个;l.remove("c") # 按元素删除
# 改:l[1]="HELLO" # 通过索引修改
# 查: 遍历 for i in l: print(i)



#n不断自减，直到变为-1时，不满足条件跳出循环

d = {'Thoms':3,'James':23}
d.get('Thoms')       #get方法 如果key不存在，可以返回None 或者自己指定的 value
d.get('Thoms',-1)    #返回None时 python不显示结果

#删除一个key 用 pop（key），对应的value也会被删除
d.pop('Thoms')
                      #dict 和 key 必须是不可变对象
s = set([1,2,3,4])
#1,2,3,4 是一个list 而显示的{1,2,3,4}只是告诉你
# 这个set内部有1,2,3,4这4个元素显示的顺序也不表示set是有序的
print(s)
s = set([1,2,2,2,3,4,5,5,5,6])
#set中重复的元素会自动被过滤
s.add(7)     #add(key)方法可以添加元素到set中，可以重复添加但不会有效
s.remove(6)  #remove方法可以删除元素
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)    #s1和s2的交集
print(s1 | s2)    #s1和s2的并集


a = 'abc'
a.replace('a','A')
print(a)

a = 'abc'
b = a.replace('a','A')
print(b)
print(a)
# a是变量，而‘abc’才是字符串对象 a本身是一个变量，它指向的对象的内容才是‘abc’
# b replace方法创建了一个新的Abc 并返回 如果用变量b指向新字符串就容易理解了 a指向原有字符串‘abc' 但变量b却指向新字符串’Abc‘了
# 所以对于不变对象来说 调用对象自身的任意方法 也不会改变该对象自身的内容 相反 这些方法创建的新的对象并返回

l = [1,2,3,4,5,6,7,11]
print(max(l))

#添加参数检查
def my_box(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#位置参数
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
#power(x,n)可以计算出任意n次方，调用时 需要传入 2个参数
#默认参数 直接把power(x,n)修改为 power(x,n=2)
#1.必选参数在前，默认参数在后，否则报错
#2.如何设置默认参数 当函数有多个参数时 把变化最大的参数放前面，变化小的放放后面
#默认参数必须指向不可变对象！！！
#可变参数
def calc(Numbers):         #让n 在Numbers中遍历
    sum = 0
    for n in Numbers:
        sum = sum + n * n
    return sum
calc([1,2,3])               # 0+1*1 0+2*2 0+3*3
#如果有一个list或者touple要调用一个可变参数可以这样操作
nums = [1,2,3]
calc(nums[0],nums[1],nums[2])  #较复杂
calc(*nums)                    #较简单


#关键字参数
def person(name,age,**kw):
    print('姓名:', name,'年龄:', age,'other:',kw)
#必选参数name age 外接受关键字参数kw 在调用该函数时只需传入必选参数
extra = {'city':'beijing','job':'manager'}
person('jack',24,**extra)
#**extra表示把extra这个字典的所有键和值用关键字参数传入到函数的**kw
#**kw将获得一个字典 注意kw获得的是一个字典的数据备份


#命名关键字
def person(name,age,**kw):
    if 'city' in kw:
        #有city 参数
        pass
    if 'job' in kw:
        #有job参数
        pass
    print('name: ', name, 'age: ', age ,'other: ', kw)
extra = {'city':'beijing','job':'manager'}
person('jack',24,**extra)

#如果要限制关键字参数的名字，就可以用命名关键字参数，只接收city和job作为关键字参数
def person(name,age,*,city,job):
    print(name,age,city,job)
person('Jack', 24, city='beijing',job='manager')

#命名关键字参数必须传入参数，这和位置参数不同，如果没有传入参数名字，调用将报错
#如果缺少* python解释器将无法识别位置参数和命名关键字参数
def person(name,age,city,job):
    #缺少*,city和job 将被视为位置参数
    pass

#参数组合 参数定义的顺序必须是 必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def d1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
d1(1,2)

#递归函数
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

#尾递归  防止栈溢出  fact(100) 报错

def fact(n):
    return fact_iter(n,1)

def fact_iter(num,produce):
    if num == 1:
        return produce
    else:
        return fact_iter(num-1,num*produce)

l = []
n = 1
while n <= 99:
    l.append(n)
    n = n+2
print(len(l))

#切片
m = [1,3,5,7,9]
print (m[0:3])
# [:3]012三位    [:-1] 倒数第一个  [-2:-1] 倒数第二个
# [:10:2]前10中每2个取一个 [：：5]所有中每5个取一个
# [:] 直接复制一个新的完全一样的
#字符串也能切片 ‘ABCDEFGHIJK’

#迭代 for循环遍历一个列表就成为迭代
#字典的迭代 默认情况下是key for key in d:
#迭代value  for value in d.values()
# 如果要同事迭代 key 和 value 可以用 for k,v in d.items()


#列表生成式
# 生成式放在前面 后面接 for循环
[x*x for x in range(1,11)]
# for循环后面可以加 if 判断
[x*x for x in range(1,11) if x % 2 ==0]
# 还可以加两层循环
[m + n for m in 'ABC' for n in 'XYZ']

import os #导入os
[d for d in os.listdir('.')] #os.listdir 可以列出文件和目录

d = {'a':'A', 'b':'B', 'c':'C'}
for k,v in d.items():
    print(k, '=', v)

#把首字母大写字母换成小写的
L = ['Groge','Keven','Paul']
for s in L:
    print(s.lower())
#生成器    generator
g = (x*x for x in range(1,11))
for n in g:
    print(n)

# 类
class Studeng(object):
    def __init__(self,name,sorce):
        self.name = name
        self.sorce = sorce

    def print_sorce(self):
        print('%s,%s' % (self.naem,self.sorce))

std = Studeng('james',88)
std.print_sorce()

# 内部访问权限 添加方法 self.__name
self.__name = name:
# 外部访问权限 在类中添加方法
def get_name(self):
    return self.__name
# 允许外部修改属性 在类中添加方法 定义方法时加上属性
def set_name(self,name):
    self.__name = name

#特殊变量 以__开头 和 以__结尾 为特殊变量
__skt__

#继承
class Animal(object):
    def run(self):
        print("Animal is running...")

#当我们要编写 dog 类和 cat 类时，可以直接继承
class Dog(Animal):
    pass

#继承父类的所有属性和方法
dog = Dog()
dog.run()
#子类继续增加方法
class Cat(Animal):
    pass
def run(self):
    print("1")

def eat(self):
    print("子类的新增方法")
# 当子类和父类都存在相同的run()方法中时，子类覆盖了父类的方法 这就叫多态
def run_two(animal):
    animal.run()
    animal.run()
# 当传入 Animal 的实例时
run_two(Animal())
# 再传入 Dog 实例 进行对比
run_two(Dog())
# 多态的好处就是 当我们需要传入Dog,Cat,Pig 时 我们只需要接收 Animal 父类的类型就可以
# 因为Dog,Cat,Pig 都是 Animal 父类 类型 按照Animal 类型进行操作
# 由于Animal 类型有run()方法 因此传入的任意类型 只要是Animal类或者子类 就会自动调用run()方法




def f(x):
    return x * x
r = map(f,[1,2,3])
# list(r) 将r 以列表打印出来 并且只能用list()打印出来
#map()函数还可以将数字转换成字符串  一行代码解决
list(map(str,[1,3,5,7]))
# reduce 函数用法  把一个函数作用在一个序列上 必须接收两个函数 拿结果再与序列的下一个元素做累计结算
# 效果如下
reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2)x3)x4)

#具体实例 str 转换成int
from functools import reduce
def fn(x,y):
    return x*10+y
def char2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
print(type(reduce(fn, map(char2num, '1738785'))))
print(reduce(fn, map(char2num, '1738785')))

# str2int 实例
from functools import reduce

def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
    return reduce(fn,map(char2num,s))

print(str2int('365779'))
print(type(str2int('365779')))

# 用lambda 简化
def str2int(s):
    return reduce(lambda x,y:x*10+y, map(lambda s:{'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s], s))


g = lambda x , y: x + y

def d_m(name, age):
    s_m = name + age
    return s_m
while True:
    print("Please tell me your name ")
    name = input("name: ")
    if name == 'q':
        break

    print("Please tell me your age")
    age = input("age: ")
    if age == 'q':
        break

b_m = d_m(name, age)
print("Hello " + b_m)

