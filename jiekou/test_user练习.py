import unittest
import requests
from bs4 import BeautifulSoup

class TestUserLogin(unittest.TestCase):
    url = 'http://115.25.108.130:5000/api/user/login/'

    #一条测试用例 必须test_开头
    def test_user_login_normal(self):
        data = {"name":"张三","password":"123456"}
        res = requests.post(url=self.url,data=data)
        self.assertIn('登录成功', res.text)            # 断言

    def test_user_login_passwd_wrong(self):
        data = {"name":"张三","password":"1234567"}
        res = requests.poast(url=self.url, data=data)
        self.assertIn('登录失败', res.text)

if __name__ == '__main__':         # 如果是直接从当前模块运行（不是从别的模块调用本模块）
    unittest.main(verbosity=2)     # 运行本测试类所有用例 verbosity 为结果显示级别



