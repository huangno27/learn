import requests
import itchat
from itchat.content import *


# 调用图灵机器人接口
KEY = '3493a2f435f345f694146819bb120de0'
UID = 'filehelper'
def get_reply(msg):
    api_tuling = 'http://openapi.tuling123.com/openapi/api/v2'
    data = {
        'key':KEY,
        'info':msg,
        'useri':UID
            }
    try:
        ret = requests.post(api_tuling,data=data).json()
        return ret.get('text')
    except:
        return

ret = get_reply('长沙天气')
print(ret)





# 对  特定的消息自动回复
@itchat.msg_register(INCOME_MSG)
def text_reply(msg):
    #print(msg)
    if not msg["FromUserName"]==myUserName:
        if msg["Text"]=="你好!":
            return "你好？"
        return "我现在有事，过会联系你"
    else:
        return "自己给自己发消息,有意思吗？"

# 定义
if  __name__ =="__main__":
    try:
        itchat.auto_login(hotReload=True)
        myUserName = itchat.get_friends(update=True)[205]["UserName"]
        itchat.run()

    except:
        print("has exccept")