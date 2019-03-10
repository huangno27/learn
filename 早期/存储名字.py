import json
username = input("what 's your name ?    ")

filename = 'username.json'
with open(filename,'w') as f_job:
    json.dump(username,f_job)
    print("We'll remember you when you come back " + username.title() + " !")
