#coding utf-8
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https:www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()

from selenium import webdriver
print(webdriver.__path__)
