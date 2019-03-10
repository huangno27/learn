filename = (r'C:\Users\13436\PycharmProjects\learnpy\All car.py')

with open(filename,encoding="utf-8") as file_object:                #添加,encoding="utf-8" 编码格式  不然会报错
    for line in file_object:
        print(line.rstrip())                                        #rstrip() 方法可以去掉不必要的空白行
