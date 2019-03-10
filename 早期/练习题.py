with open(r'C:\Users\13436\PycharmProjects\learnpy\venv\learn_python.txt') as first_name:
    duqu = first_name.read()
    print(duqu)
#zaidu = ''
#for re in duqu:
    #zaidu = re.rstrip()
#print(zaidu)



#replace()方法直接替换字符串中特定的单词
firename = (r'C:\Users\13436\PycharmProjects\learnpy\venv\learn_python.txt')
with open(firename) as first_name:
    for line in first_name:
        print(line)
line = ("In Python you can:" + 'shuxingxing').replace('Python','C')
print(line)

line = ("In Python you can:" + 'lalala').replace('Python','C')
print(line)

line = ("In Python you can:" + 'learn').replace('Python','C')
print(line)

line = ("In Python you can:" + 'xyz').replace('Python','C')
print(line)

line = ("In Python you can:" + 'learn').replace('Python','C')
print(line)

line = ("In Python you can:" + 'duquwenjian').replace('Python','C')
print(line)



username = str(input() + "please pay money")
user_name = (r'C:\Users\13436\PycharmProjects\learnpy\venv\user_name.txt')
with open(user_name,'a') as bao_cun:
    bao_cun.write(str(input()) + '\n')
    bao_cun.write(str(input()) + '\n')
    bao_cun.write(str(input()) + '\n')


#加入while循环
with open(r'C:\Users\13436\PycharmProjects\learnpy\venv\user_name.txt','a') as f:
    print("please take your name")
    loop = True
    while loop:
        input_string = input('please input something')
        if input_string != 'q':
            f.write(input_string + '\n')
        else:
            loop = False
