import requests
payload = {'key':'value','ky2':'value2'}
r = requests.post("http://httpbin.org/post",data=payload)
print(r.text)
