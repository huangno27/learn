import requests

# # 组装请求
# url = "http://httpbin.org/get"
#
# # 发送请求
# res = requests.get(url)
#
# # 解析响应
# print(res.text)

# 带参数的请求01
# url = "http://www.tuling123.com/openapi/"
# res = requests.get(url=url)
# print(res.text)
# #  带参数的请求02
# url = "http://www.tuling123.com/openapi/"
# params = { "key":"ec961279f453459b9248f0a"}
# res = requests.get(url=url,params=params)
# print(res.text)

# 传统表单类post 请求
# data 支持字典格式、字符串格式 如果是字典格式requests 方法会将其按照默认表单urlencoded合适转换为字符串格式
# 如果是字符串格式就不变
# data 以字符串格式传输需要遵循以下几条
# 1. 必须是严格的json格式字符串 里面必须用双引号 key-values 之间必须有逗号 布尔值必须是小写的true/false
# 2. 不能有中文 直接传字符串不会自动编码


url = "http://httpbin.org/post"
data = {"name":"huangyue","age":"18"}
res = requests.post(url=url,data=data)
print(res.text)

# json类型的psot 请求
url = "http://httpbin.org/post"
data = '''{ "name":"huangyue",
            "age":"18"
            }
        '''# 多行文本，字符串格式
res = requests.post(url=url,data=data)
print(res.text)

# 一般将data 声明为字典格式 然后用json.dumps()方法转化为合法的json字符串格式
# 提前引用json
import json
# url = "http://httpbin.org/post"
# data = {
#         "name":"haungyue",
#         "age":"18"
# }
# headers = {"Content_Type":"application/json"}
# res = requests.post(url=url,data=json.dumps,headers=headers)
# print(res.text)
#
# # 或者直接将字典合适的data 数据赋给post方法的json 餐宿（会自动将字典格式转化为合法json文本并添加headers）
# url="http://www.tuling123.com/openapi/api/v2"
# data = {"reqType":0,"perception":{"inputText":{"text":"附近的酒店" },"inputImage":{"url":"imageUrl"},"selfInfo":{"location":{"city":"北京","province":"北京","street":"信息路"} } },"userInfo":{"apiKey":"ec961279f453459b9248f0aeb6600bbe","userId":"206379"}}
#
# res = requests.post(url=url,data=data)
# print(res.text)

# 序列化
data = {'name':'张三','age':'18','passwd':'123456'}
set = json.dumps(data)
print(set)
# 反序列化
res_text = {'name':'\u5f20\u4e09','passwd':'123456','male':True,"money":'null'}
# 转化为字典
res_dict = json.loads(res_text)
# 获取其中的参数值
print(res_dict['name'])

# json 对象（字典）和 json 文本
# 一般在组建 data 时 用字典格式 发送请求时 转换为 json.dumps(data) 转化为文本发送请求
# 收到请求后 使用 json.loads(res.text) 转化为 字典格式 方便获取其中的参数信息

# requests 库详解
# 请求方法包含 url params data headers cookies files auth timeout

# 请求参数
# url = 字符串格式，字典格式
# params： url参数 字典格式
# data : 请求数据 字典或字符串格式
# headers ： 请求头 字典格式
# cookies ： 字典格式 可以通过携带cookie绕过登录
# files : 字典格式 用于混合表单 （from-data） 中上传文件
# auth : Basic Auth 授权 数组格式 auth = (user,passwd)
# timeout： 超时时间 防止请求一直没有响应 最长等待时间 数字格式 单位为秒

# 响应解析
# res.status_code #响应的http状态码
# res.reason # 响应的状态码含义
# res.text # 文本格式
# res.content # 响应的二进制格式
# req.encoding # 解码格式 可以通过修改 req.encoding = 'utf8'来解决一部分中文乱码
# req.apparet_encoding # 真实编码
# req.json() # 响应的json对象  慎用！！！
# req.headers # 响应头
# req.cookies # 响应的cookieJar 对象 可以通过 req.cookies.get(ket) 来获取响应中的cookie中某个key对应的值

# 需要登录的请求
# 1.使用会话保持
import requests
# 创建一个新会话
s = requests.session()
# 发送登录请求
s.post(url="https://demo.fastadmin.net/admin/index/login.html",data={"uesrname":"admin","password":"123456"})
res = s.get("https://demo.fastadmin.net/admin/index/login.html") # 使用同一个会话发送get 请求可以保持登录状态
print(res.text)

# 2.抓取cookies
# 使用谷歌访问 "https://demo.fastadmin.net/admin/index/login.html"
# f12  -> Network 查看当前请求 将 cookie 后面的复制出来 组装成字典格式


# 1和2 对比
# 使用 session 每次要发送两次请求 效率低
# 使用携带 cookies 方式 需要手动抓包 提取组装 cookies 中是session 有一定有效期 过期之后从新抓取和更换 cookies
# 如果很多或所有请求都需要登录 可以发送一次请求 保持该 session 为全局变量 其他接口都使用该session 发送请求 注意登录过期时间

# Appid或token方式
# Appid: 系统为合法用户赋予的访问id 固定的字符串 一般经过加密以确保 HTTP中的传输安全
# token:即令牌 固定或需要动态申请（有一定有效期）一般由用户信息及申请时间计算加密而成 用于验证接口访问的权限
# session 和 token 的区别
# session 是存在服务器的 服务端通过验证客户端的请求所携带的session 值在服务会话中是否存在 来验证用户是否合法
# token 是按一定算法 加密计算出来的 服务端通过解密客户端所携带的token值来验证用户是否合法

# 数字签名
# 无论cookies/session/appid/token 都只能验证请求者的身份，因此可以用抓包来篡改参数
# 数字签名 是用来对原始参数整体进行加密后生成的一个字符串 请求时参数和签名一期发送 服务器收到请求后对
# 参数再次计算签名核对和所携带者的签名是否一致

# pymysql 数据库操作
import pymysql
# conn = pymysql.connect() # 建立数据库连接
# cur.execute(sql) # 使用游标执行sql（读/写）
# cur.fetchall() # 和获取结果（读）
# cur.commit  # /提交更改（写）
# cur.close()# 关闭游标及连接
conn = pymysql.connect(host='127.0.0.1',
                       port = 3306,
                       user = 'root',
                       passwd = '123456',
                       charset = 'utf8'
                       )

# 从连接建立操作游标
cur = conn.cursor()
# 查询数据库
cur.execute("select * from user where name = '张三'")
# 获取查询结果
result = cur.fetchall()
print(result)
# 更改数据库数据
cur.execute("delect from user where name ='张三'")
# 提交更改
conn.commit() # 注意用的是conn 不是cur
# 关闭游标连接
cur.close()
conn.close()


