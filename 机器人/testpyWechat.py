import itchat


# 登录微信
itchat.auto_login(hotReload=True)

# 发送消息
# itchat.send('Hello,are u ok ?',toUserName="filehelper")
# # 发送图片         # img绝对路径
# #itchat.send("@img@img.01.jpg",toUserName="filehelper")
#
# # 获取 我的好友列表，给特定好友发消息
# friends = itchat.get_friends(update=True)
# #print(friends) # 打印好友列表 字典格式
#
# # 好友列表第一个是自己
# # 获取一个好友的信息
# first_fri = friends[1]
# print(first_fri["UserName"])
# print(first_fri["NickName"])
# print(first_fri["RemarkName"])
# # 给这位好友发送消息
# itchat.send('在吗 ? %s'%(first_fri["UserName"]),toUserName=first_fri["UserName"])
# # 给这位好友发送图片
# itchat.send("@img@img.jpg",toUserName=first_fri["UserName"])
# 搜索好友
nd_python = itchat.search_friends('媳妇')
print(nd_python)

