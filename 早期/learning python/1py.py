#猜数字
print ('-----cc------')
temp = input ("不妨猜一下心理想的是哪个数字:")
guess = int(temp)
if guess == 8:
    print("我草")
    print("哼")
else:
    print("猜错了 是8！")
print("over")
teccher = '菜鸡'
my teacher = '天黑'
docter = teacher + my teacher
print (docter)
#不限制猜的次数
print ('-----cc------')
temp = input ("不妨猜一下心理想的是哪个数字:")
guess = int(temp)
if guess == 8 :
    print("这你都知道?")
    print("不愧是菜鸡")
else:
    if guess > 8 :
        print("哥 大了大了！")
    else:
        print("小了小了")
print ("游戏结束")
#限制次数为3
import random
secret = random.randint(1,10)
count = 1
print ('----猜字谜---')
temp = input('输入你觉得对的答案')
guess = int(temp)
if guess != secret:
    while guess != secret and count < 3 :
        if guess > secret:
            print('欧巴，大了大了')
        else:
            print ('小太多哦')
        temp = input('哎呀，猜错了，再给你次机会')
        guess = int(temp)
        count = count + 1
    if guess == secret:
        print('我靠，厉害了')
        print('哼，猜中也没奖励')
    print('游戏结束咯')
#//查询成绩 elif
score = int(input("输入一个值"))
if 100 >= score >= 90:
    print("A")
elif 90 >= score >= 80:
    print("B")
elif 80 >= score >= 60:
    print("C")
elif 60 >= score >= 0 :
    print ("D")
else:
    print("请重新输入")
//while 循环
bingo = '你好'
answer = input('你想说什么?')

while True:
    if answer == bingo:
        break
    answer = input('抱歉，不是这句话')

print('聪明哦')
print('聪明的小孩儿')
    

   #for 循环
    favourite = '癞蛤蟆'
for b in favourite:
    print(b,end = '')
       
       //each
       number = ['蛤蟆', '洛瑞',  '阿三']
for each in number:
    print (each, len(number))
#取数
number = ['蛤蟆', '洛瑞',  '阿三']
for each in number:
    print (each, len(each))
# 打印2到9但是不包括9
for i in range(2,9):
    print (i)
#1到10之间成2递增
for i in range(1,10,2):
    print (i)

range ([star, ] stop[, step = 1]) #
list(range(5))
  #三元操作服
small = x if x < y else y  # if条件为真时 x = small 为假的时候 y = small
#断言 自爆
assert 3 < 4



    
