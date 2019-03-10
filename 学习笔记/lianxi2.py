class User():
    def __init__(self,first_name,last_name,login_att):
        self.first_name = first_name
        self.last_name = last_name
        self.login_att = login_att

    def desc_user(self):
        print(self.first_name.title() + self.last_name.title())

    def greet_user(self):
        print("Hello " + self.first_name + " welcome to this world !")

    def incremeng_login_att(self,abc):
        self.login_att += abc

    def reset_login_att(self,abd):
        self.login_att = abd

#ja = User('leborn','james',5)
#ja.greet_user()
#ca = User('palu','gorage',10)
#ca.greet_user()
ka = User('kobe', 'bryant',15)
ka.desc_user()
ka.incremeng_login_att(2)
print(ka.login_att)

ka.desc_user()
ka.incremeng_login_att(2)
print(ka.login_att)

ka.desc_user()
ka.incremeng_login_att(2)
print(ka.login_att)
ka.reset_login_att(0)
print(ka.login_att)
