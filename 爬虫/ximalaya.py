import json
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}
# start_url = "https://www.ximalaya.com/revision/play/album?albumId={}&pageNum={}&pageSize=30"
url = "https://www.ximalaya.com/revision/play/album?albumId={}&pageNum={}&pageSize=30"
r = requests.get(url)
ret = json.loads(r)
result = ret['data']['albums']
for i in result:
    id = i['id']
    start_url = "https://www.ximalaya.com/revision/play/album?albumId={}&pageNum={}&pageSize=30"
for i in range(7):
    url = start_url.format(i + 1)

    r = requests.get(url, headers=headers)
    ret = r.content.decode()
    #   print(ret)
    a = json.loads(ret)
    b = a["data"]["tracksAudioPlay"]
    for i in b:
        src = i['src']
    # print(src)

    ret = r.content.decode()
    a = json.loads(ret)
    b = a['data']['tracksAudioPlay']
    # print(b)
    for i in b:
        # print(i)
        src = i['src']
        name = i['trackName']
        r = requests.get(src)
        with open('1/%s.m4a' % name, 'ab') as f:
            print("正在下载：" + name)
            f.write(r.content)
            print("下载已完成！")

