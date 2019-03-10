import sys

sys.setrecursionlimit(1000000) #例如这里设置为一百万

class Ruby():
    def __init__(self,ruby_name,ruby_add):
        self.ruby_name = ruby_name
        self.ruby_add = ruby_add

    def de_ruby(self):
        print(self.de_ruby())
    def dc_ruby(self):
        print(self.dc_ruby())
    def dd_ruby(self):
        print(self.dd_ruby())

huby_c = Ruby('seven',12)
print("This 's " + huby_c.ruby_name.title() + " !")
print(str(huby_c.ruby_add) + " is working !")
duby_c = Ruby('eight',14)
print("This is your " + duby_c.ruby_name.title() + "!")


ruby = Ruby('vencent',15)                   #根据类创建实例
print("\n drop the world" + ruby.ruby_name )
print(str(ruby.ruby_add)+ " will be die")
ruby.de_ruby()                              #调用方法
ruby.dc_ruby()
ruby.dd_ruby()
bad_boy = Ruby(ruby_name,ruby_add)          #创建多个实例




class Resrant():
    def __init__(self,resranr_name,resrant_typeo):
        self.resrant_name = resranr_nam
        self.resrant_typeo = resrant_typeo
        self.number.served = 0
        self.


    def desc_resrant(self):
        print(self.desc_resrant() + "餐厅正在营业中")

    def open_resrant(self):
        print(self.open_resrant() + "餐厅正在营业中")

    def

restayrant = Resrant()



my_resrant = Resrant('seveneleven',11)
print("My restrurant is " + my_resrant.resrant_name.title() + " .")
print("My restrurant " + str(my_resrant.resrant_typeo) + " is working !")

class Computer():
    def __init__(self,replay,image):
        self.r = replay
        self.i = image
    def ad_davis(self):
        return self.ad_davis()

down = Computer(3.0,4.5)
print(down.r + down.i)

class People():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print("%s 说 : 我 %d 岁" %(self.name,self.age))

p = People('xiaohei',18)
p.speak()


class People():
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.weight = w
    def speak(self):
        print("%s 说 ： 我 %d 岁" %(self.name,self.age))

p = People('xiaobai',10,15)
p.speak()


