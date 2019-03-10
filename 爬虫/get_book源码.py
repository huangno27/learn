# -*- coding:utf-8 -*-
__author__ = "清风"

import requests
import re
from lxml import etree
# 获取小说目录，目录页面源代码
# 获取目录章节href
# 获取小说章节内容
# 下载小说

def getNovelContent():
    # 获取小说目录

    mulu_url="https://www.ybdu.com/xiaoshuo/9/9456/"

    # 提交url，获取页面源代码
    mulu_html = requests.get(mulu_url).text
    # mulu_html = requests.get(mulu_url).content

    #正则表达式  .*? 获取所有     (.*?) 分组匹配
    reg ='<li><a href="(.*?)">(.*?)</a></li>'
    urls = re.findall(reg,mulu_html)
    # print(urls)

    # 获取小说章节超链接，章节名称
    for i in urls:
        chapt_title = i[1]
        chapt_url=mulu_url+i[0]
        # 获取章节内容
        chapt_html = requests.get(chapt_url).content.decode("gbk")
        chapt_html = etree.HTML(chapt_html)
        chapt_results = chapt_html.xpath('//*[@id="htmlContent"]/text()')

        # 下载小说
        f=open("{}.txt".format(chapt_title),'w')

        for a in chapt_results:
            a = a.replace("\xa0","")
            f.write(a)
            f.write("\r\n")

        f.close()
        print("%s写入结束！！！"%chapt_title)

getNovelContent()
