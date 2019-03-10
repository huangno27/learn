import json
username = input("输入1")
try:
    with open(username) as first_name:
        username = json.load(first_name)
except FileNotFoundError:
    username = input("What 's your name ???")
    with open(username,'r') as first_name:
        json.dump(username,first_name)
        print("We'll always remember your " + username.title())
else:
    print("Welcome back" + username.title())




import json
number = input("请输入一个数字: " )
fumber = 'number.json'
with open(fumber,'w') as n_d:
    json.dump(number,n_d)
    print("I know you favrite numbei is " + str(number))

import json
fumber = 'number.json'
with open(fumber,'r') as n_d:
    json.load(fumber)
    print("读取存储的内容为" + number)

import json
number = input("请输入一个数字:")
fun = 'number.json'
with open(fun,'w') as f_d:
    json.dump(number,f_d)
    print("我就知道你会输入： " + number)