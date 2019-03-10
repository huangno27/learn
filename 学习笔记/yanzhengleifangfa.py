import unittest
from testlei import Wenjuan
class TestWenjuan(unittest.TestCase):
    """针对类的测试"""
    def test_show_question(self):
        """测试单个答案是否被存储成功"""
        question = "你喜欢什么？"
        my_answer = Wenjuan(question)
        my_answer.tj_answer('money')

        self.assertIn('money',my_answer.answers)

    def test_three_answer(self):
        """测试多个答案是否都被存储"""
        question = "你喜欢的是什么？"
        my_answer = Wenjuan(question)
        answers = ['money','big','full']
        for answer in answers:
            my_answer.tj_answer(answer)
        for answer in answers:
            self.assertIn(answer,my_answer.answers)



if __name__=='__main__':
    unittest.main()
