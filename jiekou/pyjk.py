import json
from urllib.parse import urlencode

from selenium import webdriver

def get_page_index(offset, keyword):
    data = {
        'offset': offset \
                  ',
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(data)
    browser = webdriver.PhantomJS()
    try:
        browser.get(url)
        return browser.page_source
    finally:
        browser.close()

def parse_page_index(html):
    '''解析网页资源'''
    data = json.loads(html)
    if data and 'data' in data.keys():
        '''寻找key为data的数据'''
        for item in data.get('data'):
            yield item.get('article_url')

def main():
    html = get_page_index(0, '街拍')
    '''加入如下两行代码即可'''
    html = html.replace('<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">', '')
    html = html.replace('</pre></body></html>', '')
    # print(html)
    for url in parse_page_index(html):
        print(url)

if __name__ == '__main__':
    main()
---------------------