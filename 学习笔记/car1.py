class Car():
    def __init__(self,make,size,year):
        self.make = make
        self.size = size
        self.year = year
        self.odom_reading = 0

    def get_back_name(self):
        print(str(self.year) + self.size + self.make)

    def read_odom(self):
        print("This car has " +str(self.odom_reading) +" miln go")

    def updata_odom(self,mileage):
        if mileage >= self.odom_reading:
            self.odom_reading = mileage
        else:
            print("有人改过表")

    def increment_odom(self,miles):
        self.odom_reading += miles


my_car = Car('2016','infiniti','china')
my_car.get_back_name()
my_car.odom_reading = 18         #直接改属性的值
my_car.updata_odom(20)           #将属性odom_reading的值 替换为 mileage
my_car.increment_odom(5)         #将self.odom_reading的值 递增 5
my_car.read_odom()