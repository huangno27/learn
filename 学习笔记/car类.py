class Dog():
    def __init__(self,name,age):
        """"初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """定义方法"""
        print("The " + self.name.title() + " is sitting")

    def eat(self):
        print(self.name + " is " + self.age + " years old ！")

big = Dog('小黑', '2')
big.sit()
big.eat()

your_dog = Dog('willam',6)
your_dog.sit()
print("The " + your_dog.name + " is " + str(your_dog.age) + " years")
