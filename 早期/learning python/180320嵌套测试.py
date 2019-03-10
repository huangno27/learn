# coding utf-8
emelet_ingredients = {"egg":2, "pepper":5, "mush":5}
fridge_contents = {"egg":10, "pepper":2, "mush":6}
having_ingredients = [False]
if fridge_contents["egg"] > emelet_ingredients["egg"]:   #如果第一个if不为真 他下面的任何代码都不会被求值而将被完全跳过
    having_ingredients[0] = True
    having_ingredients.append("egg")
print(having_ingredients)
if fridge_contents["mush"] > emelet_ingredients["mush"]:
    if having_ingredients[0] == False:                   #如果第一个if为真，同级的第二个条件将被计算
        having_ingredients[0] == True
        having_ingredients.append("mush")
print(having_ingredients)