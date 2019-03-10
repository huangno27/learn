#静态变量属于类，既可以使用类访问，也可以使用对象访问
class Car(object):
    type='car'

c1=Car()
print(c1.type)
print(Car.type)

#动态变量只属于对象，只能由对象访问
class Car(object):
    type='car'

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        print('我被创建了。')

c1=Car('Lamborghini','yellow')
print(c1.type)
print(Car.type)
print('name:%s,colour:%s'%(c1.name,c1.colour))


#类的动态方法是自定义的方法，同时只有对象能够调用
class Car(object):
    type = 'car'

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        print('我被创建了。')

    def show(self):
        print("The car's name is %s and colour is %s." % (self.name, self.colour))


c1 = Car('Lamborghini', 'yellow')
print(c1.type)
print(Car.type)
print('name:%s,colour:%s' % (c1.name, c1.colour))
c1.show()


#静态方法属于类，类和对象都可以进行调用
class Car(object):
    @staticmethod
    def description():
        print('This is a very fast car.')

c1=Car()
c1.description()
Car.description()

#类的属性   在方法前面加入@property装饰器，这个方法就变成了类的属性，可以以调用属性的方式进行方法的调用

class Car(object):
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    @property
    def show(self):
        print("The car's name is %s and colour is %s." % (self.name, self.colour))

c1=Car('Lamborghini','yellow')
c1.show


#私有变量  在变量前面加入两个下划线就将这个变量变为了私有变量，创建的对象没有变法访问私有变量，私有变量只能内部访问。那么私有变量怎么显示呢？

class Car(object):
    def __init__(self, name, colour):
        self.__name = name
        self.__colour = colour
    def show(self):
        print("The car's name is %s and colour is %s." % (self.__name, self.__colour))

c1=Car('Lamborghini','yellow')
c1.show()


#私有变量能在类内部定义方法进行读取。 利用类的特性也可以访问私有字段。
lass Car(object):
    def __init__(self, name, colour):
        self.__name = name
        self.__colour = colour
    def show(self):
        print("The car's name is %s and colour is %s." % (self.__name, self.__colour))
    @property
    def name(self):
        return self.__name

c1=Car('Lamborghini','yellow')
c1.show()
print(c1.name)

#私有方法  将方法前面加上两个下划线就会变成私有方法，外部就无法访问这个方法了。而如果要访问这个方法只能在类的内部才可以访问。
class Car(object):
    def __init__(self, name, colour):
        self.__name = name
        self.__colour = colour
    def __show(self):
        print("The car's name is %s and colour is %s." % (self.__name, self.__colour))
    def func(self):
        self.__show()

c1=Car('Lamborghini','yellow')
c1.func()

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