import unittest,requests,json,HTMLTestRunner
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

