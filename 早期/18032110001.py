#coding utf-8
age = 0
while True:
    how_old=input("Enter your age:")             #输入一个年龄的数字
    if how_old=="No":                            #只针对No这个单词 其他报错
        print("don't be ashamed of your age!")   #打印这不是你的年龄！
        break
        num = int(how_old)                 # 第一次自己输入的年龄 num是下次循环后第二次输入的年龄
        age = age+num                      # num是自己输入的年龄 赋值给了age每次输入的数字都会加上 上次输入的 赋值保存
        print("Your age is :")
        print(age)
        print("That is old!")
