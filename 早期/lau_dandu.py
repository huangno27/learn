import unittest
from server import Notebook
#导入


# 定义一个问题，并创建一个表示调查的Notebook对象

class TestNotebook(unittest.TestCase):       #创建测试用例
    def test_store_single_responses(self):   #定义
        """测试单个答案被妥善保存"""
        question = "What 's your favrouite language ???"
        my_server = Notebook(question)
        my_server.store_question(question)
        my_server.store_question('Eve')

        self.assertIn('Eve', my_server.responses)

if __name__=="__main()__":
    unittest.main()


s = int(input("试一试:"))
d = [1,2,3,4,5]
while True:
    if s in d:
        print("没毛病")
        break
    else:
        print("不存在")
