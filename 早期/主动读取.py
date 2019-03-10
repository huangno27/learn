import json
filename = 'username.json'
with open(filename,'r') as d_job:
    username = json.load(d_job)
    print("Welcome back  " + username.title() + " !")
