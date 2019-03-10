class Resrant():
    def __init__(self,resranr_name,resrant_typeo):
        self.resrant_name = resranr_name
        self.resrant_typeo = resrant_typeo

    def desc_resrant(self):
        print(self.desc_resrant() + "餐厅正在营业中")

    def open_resrant(self):
        print(self.open_resrant() + "餐厅正在营业中")

my_resrant = Resrant('seveneleven',11)
print("My restrurant is " + my_resrant.resrant_name.title() + " .")
print("My restrurant " + str(my_resrant.resrant_typeo) + " is working !")

your_resrant = Resrant('huanlian',9)
print("The " + your_resrant.resrant_name.title() + " is your")

class IceCreamstand(Resrant):
    def __init__(self,resranr_name,resrant_typeo):
        super().__init__(resranr_name,resrant_typeo)
        self.flavors = ['one','two','three','four','five','six']

    def cunchu(self):
        print(self.flavors)

ice = IceCreamstand('selevec',10)
ice.cunchu()

