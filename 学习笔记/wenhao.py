number = 23
s = input('现在是几点？以小时为单位 : ')
#print(type(s))

# 判断输入内容是否为数字
if s.isdigit():
    guess = int(s)
    if guess == number:
        print("晚上好")
    elif guess <= 12 and guess >= 0:
        print("早上好")
    elif guess >= 12 and guess <= 18:
        print("下午好")
    else:
        print("这不是正确时间")
else:
    print("输入有误！")

print("拜。。。")

