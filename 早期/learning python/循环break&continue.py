#coding utf-8
#for food in ("pate", "cheese", "crackers", "yogurt"):
    #if food == "yogurt":                    #判断是否有yogurt 有就循环
        #break
    #else:                                   #没有就跳出 调用else条件
        #print("sorry no food")


#for food in ("pate", "cheese", "crackers"):
    #if food == "yougurt":                     #if语句永远为false  如果条件满足false
        #break
    #else:
        #print("sorry is no :")
for food in ("tea", "water", "milk", "red apples", "cook", "milk"):
    if food[0:3] == "red":
        continue
    print("you can eat %s" % food)