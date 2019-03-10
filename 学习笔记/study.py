# -*-coding:utf-8-*-
from selenium import webdriver
import time

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com/")
        self.driver.maximize_window()
        time.sleep(2)
        self.xinlang=self.driver.find_element_by_xpath(".//*[@id='site-my-list']/ul/li[2]/a")
        time.sleep(2)
        self.xinlang.click()



    def tearDown(self):
        self.driver.quit()




    def test_baidu(self):
        all_h = self.driver.window_handles
        self.driver.switch_to.window(all_h[1])
        time.sleep(2)
        self.title = self.driver.title
        time.sleep(2)
        self.assertEqual(self.title,u"新浪首页")

# -*-coding=utf-8-*-
import HTMLTestRunner
import unittest
import danyuan.baidu


suit =unittest.TestSuite()
suit.addTest(unittest.makeSuite(danyuan.baidu.Baidu))
filename=r"C:\Users\13436\Desktop\case.html"
filen = file(filename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=filen,title=u"百度一下",description=u"测试用例")
runner.run(suit)



from selenium import webdriver
print('the first')
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('自动化测试')



def name_qm(f_name,s_name):
    full_name = f_name + s_name
    return full_name.title()
xingxing = name_qm('ran','xingxing')
print(xingxing)
daxing = name_qm('huang','huang')
print(daxing)