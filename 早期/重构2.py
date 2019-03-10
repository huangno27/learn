#2号版本 重构
import json



def get_stord_username():
    """如果存储了用户名，就获取用户名"""
    filename = 'username.json'
    try:
        with open(filename) as f_job:
            username = json.load(f_job)
    except FileNotFoundError:
       return None
    else:
        return username

def new_username():
    """提示用户输入用户名"""
    username = input("What 's your name ???")
    filename = 'username.json'
    with open(filename,'w') as f_job:
        json.dump(username,f_job)
    return username


def greet_user():
    """问候用户，并指出用户名字"""
    username = get_stord_username()
    if username:
        print("Welcome back " + username.title())
    else:
        username = new_username()
        print("We'll alwas by your side " + username.title())

greet_user()