import requests
import re



url = "https://www.jianshu.com/"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
response = requests.get(url,headers=headers)
response.encoding="_blank"
ret = response.text
result = re.findall('<a class="title" target="_blank" href="(.*?)">.*?</a>', ret)
#print(result)
for i in result:
    #print(i)
    read = "https://www.jianshu.com" + i
    print(read)
    # try:
    #     with open('1/简书' ,'wb') as f:
    #         f.write(read)
    #         f.close()
    # except Exception as e:
    #     print(e)
