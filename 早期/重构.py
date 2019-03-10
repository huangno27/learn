#1号版本
import json
def greet_user():
    """问候用户，并指出用户名字"""
    filename = 'username.json'
    try:
        with open(filename,'r') as f_job:
            username = json.load(f_job)
    except FileNotFoundError:
            username = input("What 's your name ???")
            with open(filename) as f_job:
                json.dump(username,f_job)
                print("We'll always by your side " + username.title())
    else:
        print("Welcome back " + username.title() + "!")

greet_user()




