import unittest
from name_fun import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_fun.py"""
    def test_first_last_name(self):
        """能够正确处理像xxx这种名字吗？"""
        formatted_name = get_formatted_name('jenkis','jmeter')
        self.assertEqual(formatted_name,'Jenkisjmeter')

    def test_first_middle_last_name(self):
        """能够处理中间名字吗"""
        formatted_name = get_formatted_name('1','2','3')
        self.assertEqual(formatted_name,'Acaaad')


if __name__=="__main__":
    unittest.main()