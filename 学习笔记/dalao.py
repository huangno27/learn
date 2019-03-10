#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
1.返回简单值
2.让实参变成可选
3.返回字典
4.结合使用函数和while循环

"""

'''
函数并不是总是在屏幕输出，它可以处理一些数据，并返回一个或者是一组值
'''
def get_formatted_name(first_name,last_name):
    full_name = first_name + last_name
    return full_name.title()
person0 = get_formatted_name(last_name = "胜",first_name = "陈")
print(person0)

'''
实参变为可选，则在中间加一个判断语句
'''
def get_formatted_name1(first_name,last_name,modile_name = ""):
    if modile_name:
        full_name = first_name + " "+modile_name+" "+last_name
    else:
        full_name = first_name + " "+last_name
    return full_name.title()

person1 = get_formatted_name1(last_name = "sheng",first_name = "cheng")
print(person1)

person2 = get_formatted_name1(last_name = "sheng",modile_name = "zhnag",first_name = "cheng")
print(person2)

'''
1.函数可以返回任何类型的值，包括列表或者是字典这种复杂的数据结构
'''
def person_name(name,age,sex,job):
    ''' Returns a dictionary containing a person's information '''
    person = {"name":name,"age":age,"sex":sex,"job":job}
    return person
person3 = person_name(name = "张敞",age = "27",sex = "男",job = "精算师")
print(person3)

"""
结合使用函数和while循环，循环上面的字典，打印信息，并且用户可以退出
"""


