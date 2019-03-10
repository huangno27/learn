import requests,os,json,re
from scrapy.selector import Selector

class wangyiyun():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Referer': 'http://music.163.com/'}
        self.main_url='http://music.163.com/'
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def get_songurls(self,playlist):
        '''进入所选歌单页面，得出歌单里每首歌各自的ID 形式就是“song?id=64006"'''
        url=self.main_url+'playlist?id=%d'% playlist
        re= self.session.get(url)   #直接用session进入网页，懒得构造了
        sel=Selector(text=re.text)   #用scrapy的Selector，懒得用BS4了
        songurls=sel.xpath('//ul[@class="f-hide"]/li/a/@href').extract()
        return songurls   #所有歌曲组成的list

    def get_songinfos(self,songurls):
        '''根据songid进入每首歌对应的url，拿到歌手名字，url就是:"http://music.163.com/song?id=64006"'''
        for songurl in songurls:
            url=self.main_url+songurl
            re=self.session.get(url)
            sel=Selector(text=re.text)
            song_id = url.split('=')[1]
            song_name = sel.xpath("//em[@class='f-ff2']/text()").extract_first()
            singer= '&'.join(sel.xpath("//p[@class='des s-fc4']/span/a/text()").extract())
            print(song_id,song_name,singer)

    def work(self,playlist):
        songurls=self.get_songurls(playlist)
        self.get_songinfos(songurls)

d=wangyiyun()
d.work(2214059025)
