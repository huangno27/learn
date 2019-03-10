#很鸡巴复杂啊
#私有变量
class Cra():
    def __init__(self,name,color):
        self.__name = name                    #双下划线将变量变为私有变量
        self.__color = color

    #@property                                #设置私有变量的另一种方法
    def show(self):
        print("The car's name is %s and color is %s ." %(self.__name,self.__color))
    def func(self):
        self.show()

class Bro(Cra):
    def __init__(self,name,color):
        super().__init__(name,color)

    def drop_word(self):
        print("这是子类的方法" )


c1 = Cra('infiniti','white')
c1.func()

d1 = Cra('audi','white')
d1.func()

f1 = Bro('bora','black')
f1.drop_word()


#私有方法
class Car(object):
    def __init__(self,name,color):
        self.__name = name
        self.__color = color

    def __show(self):                 #私有方法 加双下划线
        print("打印私有变量")

    def func(self):
        self.__show()

a1 = Car('infiniti','blcak')
a1.func()                              #调用方法时不是直接调用私有方法


#私有变量更改
class Car(object):
    def __init__(self, name, colour):
        self.__name = name
        self.__colour = colour
    def show(self):
        print("The car's name is %s and colour is %s." % (self.__name, self.__colour))
    @property
    def func(self):
        return self.__name
    @func.setter
    def func(self,value):
        self.__name=value

c1=Car('Lamborghini','yellow')
c1.show()
c1.func='car'
c1.show()

# _del_()函数和_init_()方法使用的一样
# __Call__方法
class Car(object):                        #当对象作为一个函数进行执行的时候，就会执行这个方法。
    def __call__(self, *args, **kwargs):
        print('call')

c1=Car()
c1()