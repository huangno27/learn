import requests

url = 'https://www.baidu.com'
r = requests.get(url)
print("status code: " ,r.status_code)

#将API响应存储在一个变量中
requests_dict = r.json()

#处理结果
print(requests_dict.keys())

