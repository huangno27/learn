#!/use/bin/env python 3.7
def in_fridge():

    try:
        count = fridge[wanted_food]
    except KeyError:
        count = 0
    return count




import random
secret = random.randint(1,10)
temp = input("猜猜看:")
guess = int(temp)
while guess != secret:
    temp = input("猜错了，再来一次:")
    guess = int(temp)
    if guess == secret:
        print('对哦')
        print('聪明')
    else:
        if guess >=secret:
            print('错错错，大大大！')
        else:
            print('错错错，小小小！')
    print('GAME OVER')



    strs = ("1", "2", "3")
    def test(name):
        if strs[0] == name:
            print("First: " + strs[0])
        elif strs[1] == name:
            print("Second: " + strs[1])
        else:
            print(strs[2])
