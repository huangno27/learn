#coding utf-8
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https:www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
quit()

import requests

req = requests.get(url = 'www.baidu.com')
