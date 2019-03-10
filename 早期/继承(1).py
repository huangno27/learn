class Car():
    def __init__(self,make,year,drr):
        self.make = make
        self.year = year
        self.drr = drr

    def get_name(self):
        print(self.make)

    def get_all(self):
        print(self.make + " " + str(self.year) + " " + self.drr)

    def fill_gas_tank(self):  #父类中与子类相同的方法名字 但是子类用不到这个方法 需要在子类中重写
        print("这是父类的方法")


class Newlei():
    def __init__(self,long_time = 70):
        self.long_time = long_time

    def desc_battery_size(self):                      #将子类的方法注释掉，修改到新的类 当做实例 再当成子类的属性调用
        print("这是在调用实例用作属性")

    def get_range(self):
        """打印电瓶车的续航里程"""
        if self.long_time == 70 :
            range = 240
        elif self.long_time == 85:
            range = 270

        message = "This car can go " + str(range)
        message += " do you know ?"
        print(message)






#创建新的类

class Dacar(Car):                                                 #创建子类时 父类必须包含在文件中 且父类位于子类前面 car 在 dacar  前面
    def __init__(self,make,year,drr):
                                                                  #方法_init_()接受创建car实例所需的信息
        super().__init__(make,year,drr)                           #super()是一个特殊函数 将父类和子类关联起来，让子类继承父类的所有属性和方法
        self.newlei = Newlei()                                    # 为新的子类创建属于子类的属性 self.后面字母小写

    #def desc_long_time(self):                                     #为新的子类创建方法 用来调用上面新增的属性 最后用新实例调用这个方法 确认子类方法可用
        #print("这是子类的属性 " +str(self.long_time) + " !")

    #可以根据子类创建任意的属性和方法用来描述子类（电动车）
    #但如果一个属性或方法是任何汽车都有的，而不是子类特有的（电动车）就应该将这个属性或方法添加到父类中再去调用
    #子类只包含处理子类（电动车）特有属性和行为的代码


    #重写父类的方法：如果父类中有一个方法，与子类模拟的实物不相符，都可对其重写
    #可在子类中定义一个方法，它与要重写的父类方法同名，python不关注父类中的方法，而只关注你在子类中定义的相应方法
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("这是子类的方法")




my_car = Dacar('infiniti','2016','china')
#print(my_car.make + " " + str(my_car.year) + " " + my_car.drr)
my_car.get_all()
print(my_car.year)
#my_car.desc_long_time()                                                           #将之间子类的方法注释掉 重新写
my_car.newlei.desc_battery_size()                                                  #实例的首字母要小写 不然报错
my_car.fill_gas_tank()
#print("This car doesn't need a gas tank " + str(my_car.fill_gas_tank()))          #没必要加这句代码
my_car.newlei.get_range()