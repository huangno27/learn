# https://cuiqingcai.com/3179.html 爬虫教程原文
# https://blog.csdn.net/baidu_35085676/article/details/68958267?locationNum=15&fps=1  翻译 + 多线程
import requests
from bs4 import BeautifulSoup
import os
import re

Hostreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://www.389abc.com'
}
Picreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://www.389abc.com'
}


def get_page_name(url):  # 获得图集最大页数和名称
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    span = soup.findAll('span')
    title = soup.find('h2', class_="main-title")
    return span[10].text, title.text


def get_html(url):  # 获得页面html代码
    req = requests.get(url, headers=Hostreferer)
    html = req.text
    return html


def get_img_url(url, name):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    img_url = soup.find('class', title=name)
    #  img 网页源代码搜索   alt='丰胸美臀前凸后翘 绝世尤物Egg尤妮丝女人味十足
    return img_url['data-original']


def save_img(img_url, count, name):
    req = requests.get(img_url, headers=Picreferer)
    new_name = rename(name)
    # 图片不是文本文件，以二进制格式写入，所以是html.content
    with open(new_name + '/' + str(count) + '.jpg', 'wb') as f:
        f.write(req.content)


def rename(name):
    rstr = r'[\/\\\:\*\?\<\>\|]'
    new_name = re.sub(rstr, "", name)
    return new_name


def save_one_atlas(old_url):
    page, name = get_page_name(old_url)
    new_name = rename(name)
    os.mkdir(new_name)

    # 输出每个图片页面的地址
    print("图集--" + name + "--开始保存")
    for i in range(1, int(page) + 1):
        url = old_url + "/" + str(i)
        img_url = get_img_url(url, name)
        # print(img_url)
        save_img(img_url, i, name)
        print('正在保存第' + str(i) + '张图片')
    print("图集--" + name + "保存成功")


def get_atlas_list(url):
    req = requests.get(url, headers=Hostreferer)
    soup = BeautifulSoup(req.text, 'lxml')
    atlas = soup.find_all(attrs={'class': 'col-md-3 col-sm-6 col-xs-12 clearfix news-box'})
    atlas_list = []
    for atla in atlas:
        atlas_list.append(atla.parent['href'])
    return atlas_list


def save_one_page(start_url):
    atlas_url = get_atlas_list(start_url)
    for url in atlas_url:
        save_one_atlas(url)


if __name__ == '__main__':
    start_url = "http://www.389abc.com/"
    for count in range(1, 3):
        url = start_url + "page/" + str(count) + "/"
        save_one_page(url)
    print("爬取完成")
