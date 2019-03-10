import itchat
from itchat.content import *

# 对  特定的消息自动回复
@itchat.msg_register(INCOME_MSG)
def text_reply(msg):
    #print(msg)
    if not msg["FromUserName"]==myUserName:
        if msg["Text"]=="你好!":
            return "你好？"
        return "你长得好像一个笑话"
    else:
        return "自己给自己发消息,有意思吗？"
# 报错了
# @itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
# def single_msg_register(msg):
#     if msg['Type'] == TEXT:
#         defaultReply = 'I show' + msg['TEXT']
#         print(msg['TEXT'])
#         if msg['TEXT'] in ["笑话","讲笑话"]:
#             reply = "你长得就像个笑话···"
#         else:
#             reply = get_reply(msg['TEXT'])
#         return reply or defaultReply
#     return

# 定义
if  __name__ =="__main__":
    try:
        itchat.auto_login(hotReload=True)
        myUserName = itchat.get_friends(update=True)[205]["UserName"]
        itchat.run()

    except:
        print("has exccept")