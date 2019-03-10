filename = (r'C:\Users\13436\PycharmProjects\learnpy\All car.py')
with open(filename,encoding="utf-8") as new_object:
    lines = new_object.readlines()
for re in lines:                          #已经在with模块外 使用for循环调用lines
    print(re.rstrip())


#引用文件内容

filename = (r'C:\Users\13436\PycharmProjects\learnpy\All car.py')
with open(filename,encoding="utf-8") as first_name:
    lines = first_name.readlines()

kong_cunchu = ''
for re in lines:
    kong_cunchu += re.strip()             #rstrip()和strip()的区别
print(kong_cunchu)
print(len(kong_cunchu))

#包含一百万位的大型文件,精确到小数点后面50位
filename = (r'C:\Users\13436\PycharmProjects\learnpy\All car.py')
with open(filename,encoding="utf-8") as second_naem:
    lines = second_naem.readlines()
kong_cunchu = ''
for re in lines:
    kong_cunchu += re.rstrip()
print(kong_cunchu[:50] + "...")
print(len(kong_cunchu))

#输入一个字符串 检验这个字符串是否在列表中
birthday = input("Enter your birthday :" )
if birthday in lines:
    print("你的生日在列表中")
else:
    print("你的生日不在列表中")
