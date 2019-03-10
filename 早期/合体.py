import json
filename = 'username.json'
try:
    with open(filename) as d_job:
        username = json.load(d_job)
except FileNotFoundError:
    username = input("What 's your name ???   ")
    with open(username,'w') as d_job:
        json.dump(username ,d_job)
        print("We'll remember your name !!!" + username.title() + " ever and ever")
else:
    print("Welcome back  " + username.title())


