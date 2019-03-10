import urllib.request
import re
# 1 获取主页源代码
# 2 获取章节超链接
# 3 获取章节超链接源码
# 4 获取小说内容
# 5 下载,文件操作

# 驼峰命名法
##获取小说内容
def getNovertContent():
    # <http.client.HTTPResponse object at 0x000001DFD017F400>
    html = urllib.request.urlopen("https://book.qidian.com/info/1209977").read()
    html = html.decode("_blank")
    # 不加括号  不匹配
    # 正则表达式  .*?  匹配所有
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    # 增加效率的
    reg = re.compile(reg)
    urls = re.findall(reg,html)
    print(urls)
    # print(urls)
    # 列表
    # [(http://www.quanshuwang.com/book/0/269/78850.html,第一章 山边小村),
    # (http://www.quanshuwang.com/book/0/269/78854.html,第二章 青牛镇)]
    for url in urls:
        # 章节的URL地址
        novel_url = url[0]
        # 章节标题
        novel_title = url[1]

        chapt = urllib.request.urlopen(novel_url).read()
        chapt_html = chapt.decode("gbk")
        # r 表示原生字符串   \ \\d  r"\d"
        reg = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'
        # S 代表多行匹配
        reg = re.compile(reg,re.S)
        chapt_content = re.findall(reg,chapt_html)
        # print(chapt_content)
        # 列表["&nbsp;&nbsp;&nbsp;&nbsp二愣子睁大着双眼，直直望着茅草和烂泥糊成的<br />"]

        # 第一个参数   要替换的字符串   替换后的字符串
        chapt_content = chapt_content[0].replace("&nbsp;&nbsp;&nbsp;&nbsp;","")
        # print(chapt_content)    字符串  二愣子睁大着双眼，直直望着茅草和烂泥糊成的<br />
        chapt_content = chapt_content.replace("<br />","")

        print("正在保存 %s"%novel_title)
        # w 读写模式  wb
        # f = open("{}.txt".format(novel_title),'w')
        # f.write(chapt_content)

        with open("{}.txt".format(novel_title),'w') as f:
            f.write(chapt_content)

        # f.close()

getNovertContent()