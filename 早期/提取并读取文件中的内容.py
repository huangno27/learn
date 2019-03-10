import csv

#获取文件内容
filename = (r'C:\Users\13436\PycharmProjects\learnpy\csv_dict_data1.csv')
with open(filename) as f:
    reader = csv.reader(f)
    header_now = next(reader)

#读取指定索引的值
    highs = []
    for row in reader:                       #用int()将字符串转换成数字   highs = int(row[1])  \n highs.append(high)
        highs.append(row[1])

    print(highs)