import json
print(json.__all__)

# 定义一个字典 通过json 把它序列化未json格式的字符串
import json
dicti={'name':'leizi','age':'27','address':'北京'}

print(u'未序列化钱的数据类型为：',type(dicti))
print(u'未序列化钱的数据：',dicti)

# 对dicti进行序列化的处理

stri=json.dumps(dicti)
print(u'未序列化钱的数据类型为：',type(stri))
print(u'未序列化钱的数据：',stri)

# 反序列化 把json格式的字符串解码为python的数据对象
import json
dicti={'name':'leizi','age':'27','address':'北京'}
print(u'未序列化钱的数据类型为：',type(dicti))
print(u'未序列化钱的数据：',dicti)
# 对dicti进行序列化的处理
stri=json.dumps(dicti)
print(u'未序列化钱的数据类型为：',type(stri))
print(u'未序列化钱的数据：',stri)
# 对stri进行反序列化
dicti2=json.loads(stri)
print(u'未序列化钱的数据类型为：',type(dicti2))
print(u'未序列化钱的数据：',dicti2)

# 结合requests 库 来看返回的json数据
import json,requests
r=requests.get("http://wthrcdn.etouch.cn/weather_mini?city=北京")
print(r.text,u'数据类型:',type(r.text))
# 对数据进行反序列化的操作
dic=json.loads(r.text)
print(dic,u'数据类型:',type(dic))

# 使用python进行组织编写接口测试用例
# 1.拿到接口的url地址
# 2.查看接口是用什么方式发送
# 3.添加请求头，请求体
# 4.发送查看返回结果，校验返回结果是否正确

import requests
# 接口的url
url = "http://fanyi.baidu.com/v2trabsapi"
# 接口的参数
params = {
    "from":"en",
    "to":"zh",
    "query":"teat"
}
# 发送接口
r=requests.request("post",url,params=params)

# 打印返回结果
print(r.text)

# 其实到上面已经完成了 因为百度不是自己写的接口 为了让结果看的更加清楚
# 我取来翻译的字段
import json
d=json.loads(r.text)
print(d['liju_result']['tag'])
