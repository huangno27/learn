class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def defcribe_res(self):
        print("The " +self.restaurant_name + " for your")
        print("The " +self.cuisine_type + " is so big")

    def open_res(self):
        print("The" + self.restaurant_name + " is working")
restaurant = Restaurant('seven','8')
print(restaurant.restaurant_name + str(restaurant.cuisine_type))
rdc = Restaurant('a','b')
rdc.defcribe_res()
rec = Restaurant('a','d')
rec.defcribe_res()
rfc = Restaurant('a','g')
rfc.defcribe_res()