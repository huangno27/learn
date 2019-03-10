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


#创建新的实例 将把这个实例当做子类的属性来用
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



#创建子类  将子类中与上面新建的实例中相同方法注释掉

class Dacar(Car):                                                 #创建子类时 父类必须包含在文件中 且父类位于子类前面 car 在 dacar  前面
    def __init__(self,make,year,drr):
                                                                  #方法_init_()接受创建car实例所需的信息
        super().__init__(make,year,drr)                           #super()是一个特殊函数 将父类和子类关联起来，让子类继承父类的所有属性和方法
        self.newlei = Newlei()                                    # 为新的子类创建属于子类的属性 self.后面字母小写

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("这是子类的方法")


my_car = Dacar('infiniti','2016','china')
my_car.get_all()
my_car.newlei.desc_battery_size()
my_car.newlei.get_range()
my_car.fill_gas_tank()
