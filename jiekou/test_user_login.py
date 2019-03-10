import unittest
import requests
from read_excel import *
import json

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list("test_user_data.xlsx","TestUserLogin")

    def test_user_login_normal(self):
        case_data = get_test_data(self.data_list,'test_user_login_normal')
        if not case_data:
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        res = requests.post(url=url,data=json.loads(data))
        self.assertEqual(res.text,expect_res)

if __name__ == '__main__':
    unittest.main(verbosity=2)

