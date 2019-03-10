# 拆分请求 注意agent是请求的身份 如果没有agent 那么服务器一定不会响应 所以可以在 headers 中设置agent
import urllib
import urllib2
url = 'http://www.server.con/login'
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
values = {'username':'cpc','password':'xxxxxx'}
headers = {'User-agent':user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url,data,headers)
reponse = urllib2.urlopen(request)
page = reponse.read()
# 这样就设置好一个headers 在构建request时传入 在请求时加入了headers的传送
# 服务器若识别了就会得到响应
#另外 还有对付“反链接”的方式 队伍防盗链，服务器会是被headers中的referer是不是它自己
#如果不是 有的服务器不会响应 所以还要在headers中加入referer
headers = {'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
           'Referer':'http://www.zhihu.com/articles'}
#同上面的方法传送时加入这个就可以应付防盗链了
#headers 的一些属性 需要特别注意
# User-Agent : 游戏服务器或Proxy会通过该值来判断师傅是浏览器发出的请求
# Conter-Type: 在使用REST接口时 服务器会检查该值 用来确定HTTP Body 中的内容该怎样解析
# applicatiom/xml: 在XML RPC 如RESTful/SOAP 调用时使用
# application/json： 在JSON RPC 调用时使用
# applocation/x-www-form-urlencoded: 浏览器提交web 表单时使用
# 在使用服务器提供的Restful或SOAP服务时，Content-Type 设置错误会导致服务器拒绝服务


# Proxy（代理）设置
#urllib2 默认会使用环境变量http_proxy来设置HTTP Proxy 例如一个网站会检测某一时段某个IP的访问次数
#如果次数过多它会禁止你的访问 所以可以社会一些代理服务器来帮助工作 每隔一段时间换一个代理 网站就不知道是谁在搞鬼了

import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

# Timeout设置
# 参数Timeout的设置 可以设置等待多久超时 为了解决一些网站是在响应过慢而造成的影响
# 下面代码 如果第二个参数data为空那么也别指定是timeout是多少 写明形参
import urllib2
response = urllib2.urlopen('http://www.baidu.com',timeout=10) #如果data为空需要特别指定timeout是多少
import urllib2
response = urllib2.urlopen('http://www.baidu.com',data,10)    #如果data 已经传入 则不必声明

#使用HTTP的 PUT 和 DELETE 方法
#http 有六种请求方法 get head put delete post options 我们有时候需要用到 put 和 delete 方式请求
import urllib2
request = urllib2.Request(uri,data=data)
request.get_method = lambda:'PUT'#or 'DELETE'
response = urllib2.urlopen(request)

#使用 DebugLog
#可以通过下面的方法把debuglog打开 这样收发包的内容就会在屏幕上打印出来，方便调试，这个也不太常用
import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglebel=1)
opener = urllib2.build_opener(httpHandler,httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen("http://www.baidu.com")
#在后面还有cookies的设置还有异常的处理

#异常处理 URLError  和 HTTPError
#首先解释下产生error的原因
# 1.网络无法连接，即本机无法上网
# 2.连接不到指定的服务器
# 3.服务器不存在
#在代码中我们需要用 try_expect 语句来捕获相应的异常
import urllib2
request = urllib2.Request('http://www.xxxx.com')
try:
    urllib2.urlopen(request)
except urllib2.URLError,e:
    print e.reason
# HTTPError 是 URLError 的子类在你利用urlopen方法发出一个请求时 服务器上都会对应一个应答对象response
# 其中包含一个数字“状态码”
# 错误码太多 看截图

#cookie 某些网站为了辨别用户身份，进行session跟踪而存储在用户本地终端上的数据（通常经过加密）
#比如说有些网站需要登录后才能访问某个页面，你想抓取某个页面内容是不允许的 那么可以利用urllib2库保存我门登录的cookie
# 然后抓取其他页面打到目的
# opener 概念：当你获取一个url 你使用opener（一个urllib2.OpenerDirector的实例）在前面我门是使用的默认的opener
# 也就是urlopen 它是一个特别的opener 可以理解成opener的一个特殊实例传入的参数仅仅是url data timeout
# 如果我们需要cookie 只用这个opener是达不到目的的所以我们需要创建更一般的opener来实现对cookie的设置
# cookielib 这个模块的主要作用是提供可存储cookie的对象 以便于与urllib2模块配合使用internet资源
# 这个模块非常强大 我们可以利用本模块的cookiejar类的对象来捕获cookie并在后续链接请求时重新发送 比如实现模拟登陆功能
# 该模块主要的对象有 cookiejar filecookiejar mozillacookiejar lwpcookiejar
# 获取cookie保存到变量
import urllib2
import cookielib
#声明一个cookiejar对象实例来保存cookie
cookie = cookielib.Cookiejar()
#利用urllib2库的 HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCooikeProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的uelopen方法 也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'NAME = '+item.name
    print 'Value= '+item.value
# 保存cookie到文件
import cookielib
import urllib2
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCooikeProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True,ignore_expires=True)


# 利用cookie模拟网站登陆
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
    'stuid':'201200131012',
    'pwd':'12345678'
})
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbkscjcx.curscopre'
result = opener.open(gradeUrl)
print result.read()

# 正则表达式：对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符，及这些特定字符的组合。
# 组成一个‘规则字符串’这个规则字符串用来表达对字符串的一种过滤逻辑。
# 正则表达式是用来匹配字符串非常强大的工具，想要从返回的页面内容中提取出想要的内容就易如反掌了
# 匹配过程 1.一次拿出表达式和文本中的字符比较
# 2.如果每一个字符都能匹配则匹配成功，一旦有匹配不成功的字符则匹配失败
# 3.如果表达式中有量词或边界，这个过程稍微有些不同
# 正则贪婪模式与非贪婪模式 例如‘ab’ 用于查找‘abbbc’ 贪婪模式将找到abbb 非贪婪模式'ab'找到‘a’
# 一般使用非贪婪模式用来提取
# 反斜杠 ‘\’用于表示转义符 py中可以使用 r"\"表示 匹配一个数字的 “\d” 可以写成 r“\d”
# 实例
import re
#将正则表达式编译成Pattern对象 注意hello前面的r的意思是”原生字符串“
pattern = re.compile(r'hello')

#使用re.match匹配文本 获得匹配结果 无法匹配则返回none
result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloo CQC!')
result3 = re.match(pattern,'helo CQC!')
result4 = re.match(pattern,'hello CQC!')
# 如果1匹配成功
if result1:
    #使用match获得分组信息
    print result1.group()
else:
    print '1不匹配'

if result2:
    #使用match获得分组信息
    print result2.group()
else:
    print '2不匹配'

if result3:
    #使用match获得分组信息
    print result3.group()
else:
    print '3不匹配'

if result4:
    #使用match获得分组信息
    print result4.group()
else:
    print '4不匹配'


import re
m = re.match(r'(\w+)(\w+)(?P.*)','(hello word)')

#print "m.string",m.string   #匹配时使用的文本
#print "m.re",m.re           #匹配时使用的Pattem对象
#print "m.pos",m.pos         #文本中正则表达式开始搜索的索引 值与Pattem.match()和Pattem.seach()方法的同名参数相同
#print "m.endpos",m.endpos   #文本中正则变大时结束搜索的索引 值与Pattem.match()和Pattem.seach()方法的同名参数相同
