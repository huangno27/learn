class Car():
    def __init__(self,make,model,year,login_attempts,miles):
        self.make = make
        self.model = model
        self.year = year
        self.login_attempts = 0


    def get_desc_name(self):
        long_name = str(self.year + " " + self.make + " " + self.model)
        return long_name

    def read_login_arrempts(self):
        print("This is " + str(self.login_attempts) + "!")

    def update_login_attenpts(self,mileage):
        self.login_att = mileage


    def increment_login_attempts(self,miles):
        self.login_attempts += miles

    def reset_login_attempts(self,milk):
        self.login_attempts = milk             #TypeError: reset_login_attempts() missing 1 required positional argument: 'milk'
                                                             #缺少一个位置的参数

my_new_car = Car('infinidi', '4s', '2015','0','0')
print(my_new_car.get_desc_name())

my_new_car.update_login_attenpts(10)
my_new_car.read_login_arrempts()

my_new_car.increment_login_attempts(1)
my_new_car.read_login_arrempts()

my_new_car.read_login_arrempts()
my_new_car.read_login_arrempts()

my_new_car.reset_login_attempts()
my_new_car.login_attempts = 0
my_new_car.read_login_arrempts()

dj_car = Car('audi','yiqi','2016','1')
dj_car.increment_login_attempts(1)


fj_car = Car('aotu','qixi','2004','2')
fj_car.increment_login_attempts(3)
