# 使用python进行组织编写接口测试用例
# 1.拿到接口的url地址
# 2.查看接口是用什么方式发送
# 3.添加请求头，请求体
# 4.发送查看返回结果，校验返回结果是否正确

import requests
import json
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

# import json
try:
    d=json.loads(r.text,)             # 不用try expect的话 报错 json数据格式有问题
    print(d['liju_result']['tag'])
except:
    pass
print("1")


#  unittest 库优化
import unittest,requests,json
class Testbaiduapi(unittest.TestCase):
    def setUp(self):
        url = "http://fanyi.baidu.com/v2trabsapi"
    def testzhen(self):
        params={
            "from": "en",
            "to": "zh",
            "query": "teat"
}
        url = "http://fanyi.baidu.com/v2trabsapi"
        r = requests.request("post",url,params=params)
        r=json.loads(r.text)
        assert u'学习' in r['liu_result']['tag']
    def testzhen1(self):
        params={
            "from":"en",
            "to":"h",
            "query":"std"
        }
        url = "http://fanyi.baidu.com/v2trabsapi"
        r = requests.request("post",url,params=params)
        r=json.loads(r.text)
        assert u'学' in r['liu_result']['tag']
    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main(verbosity=2)






