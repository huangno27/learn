class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.login_attempts = 0


    def get_desc_name(self):
        long_name = str(self.year + " " + self.make + " " + self.model)
        return long_name
    def read_login_arrempts(self):
        print("This is " + str(self.login_attempts) + "!")


my_new_car = Car('infinidi', '4s', '2015')
print(my_new_car.get_desc_name())
my_new_car.read_login_arrempts()
