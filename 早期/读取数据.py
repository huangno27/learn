with open(r'C:\Users\13436\PycharmProjects\learnpy\All car.py',encoding="utf-8") as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    print(len(contents))


import json
username = input("What 's your name ??? ")
filename = 'usranem.json'
with open(filename,'w') as f_job:
    json.dump(username,f_job)

import json
fname = 'username.json'
with open(fname,'r') as d_jof:
    json.load(d_jof)
    print("Welcome back " + username.titlt())

import json
fckname = 'username.json'
try:
    with open(fckname) as first_name:
        username = json.load(first_name)
except FileNotFoundError:
    username = input("What 's your name ???")

    with open(filename,'r') as second_name:
        json.dump(username,second_name)
        print("We'll always remember your " + username.title())
else:
    print("Welcome back" + username.title())