# import requests
#
# url = "https://dig.chouti.com/"
# headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
# post_dict = {'phone':'864426',
#              'password':'huang134',
#              'oneMonth':1
#              }
#
# response = requests.post(url = url,
#                         data = post_dict,
#                         headers = headers)
# #print(response.text)
# cookie_dict = response.cookies.get_dict()
# print(cookie_dict)
#
# response = requests.get(
#     url = "https://dig.chouti.com/profile",
#     cookies=cookie_dict)
# print(response.text)

#gpsd=c9717a44cdd5d8fc03b51af7449cb04f


import requests

session = requests.Session()

### 1、首先登陆任何页面，获取cookie
i1 = session.get(url="http://dig.chouti.com/help/service")

### 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
i2 = session.post(
    url="http://dig.chouti.com/login",
    data={
        'phone': "8615131255089",
        'password': "woshiniba",
        'oneMonth': ""
    }
)

i3 = session.post(
    url="http://dig.chouti.com/link/vote?linksId=11837086",
)
print(i3.text)