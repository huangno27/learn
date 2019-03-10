import requests
from lxml import etree

class Spider(object):
    def start_request(self):
        reponse = requests.get("https://ibaotu.com/shinin/")
        content = reponse.content.decode()
        html = etree.HTML(content)
        src_list = html.xpath('//div[@class="video-play"]/video/@src')
        tit_list = html.xpath('//span[@class="video-title"]/text()')
        self.xpath_data(src_list,tit_list)

    def xpath_data(self,src_list,tit_list):
        for src,tit in zip(src_list,tit_list):
            cd = requests.get("http:" + src).content
            filename = tit + ".mp4"
            print("正在爬取"+ filename)
            try:
                with open('imgs/%s' % filename[-10:],"wb") as f:
                    f.write(cd.content)
            except Exception as e:
                print(e)
                pass


print("0")
s = Spider()
s.start_request()