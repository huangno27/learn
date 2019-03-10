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
        print("Hello")


#创建新的类

class Dacar(Car):                                                 #创建子类时 父类必须包含在文件中 且父类位于子类前面 car 在 dacar  前面
    def __init__(self,make,year,drr):
                                                                  #方法_init_()接受创建car实例所需的信息
        super().__init__(make,year,drr)                           #super()是一个特殊函数 将父类和子类关联起来，让子类继承父类的所有属性和方法
        self.long_time = 70                                       # 为新的子类创建属于子类的属性

    def desc_long_time(self):                                     #为新的子类创建方法 用来调用上面新增的属性 最后用新实例调用这个方法 确认子类方法可用
        print("That 's have " +str(self.long_time) + " !")

    #可以根据子类创建任意的属性和方法用来描述子类（电动车）
    #但如果一个属性或方法是任何汽车都有的，而不是子类特有的（电动车）就应该将这个属性或方法添加到父类中再去调用
    #子类只包含处理子类（电动车）特有属性和行为的代码


    #重写父类的方法：如果父类中有一个方法，与子类模拟的实物不相符，都可对其重写
    #可在子类中定义一个方法，它与要重写的父类方法同名，python不关注父类中的方法，而只关注你在子类中定义的相应方法
    def fill_gas_tank(self):
        """电动汽车没有邮箱"""
        print("This car doesn't need a gas tank")




my_car = Dacar('infiniti','2016','china')
#print(my_car.make + " " + str(my_car.year) + " " + my_car.drr)
my_car.get_all()
print(my_car.year)
my_car.desc_long_time()
my_car.fill_gas_tank()
#print("This car doesn't need a gas tank " + str(my_car.fill_gas_tank()))   #没必要加这句代码

