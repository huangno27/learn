class Res_0():
    def __init__(self,res_name,cui_typ):
        self.res_name = res_name
        self.cui_typ = cui_typ
        self.number_served = 15

    def desc_res(self):
        print(self.res_name)

    def open_res(self):
        print(self.res_name)

    def serving_number(self):
        print("This res today has " + str(self.number_served) +" been")

    def update_number(self,mileage):  #通过方法修改属性的值，定义一个新的方法 让初始值=新方法的属性
        self.number_served = mileage


res = Res_0('buy',10)
print(res.res_name.title())
print(str(res.cui_typ) + "你有吗")
#res.desc_res()
#res.open_res()
res.update_number(12) #调用新增加修改初始值的那个方法
res.serving_number()  #调用


