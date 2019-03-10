import csv
filename = (r'C:\Users\13436\PycharmProjects\learnpy\csv_dict_data1.csv')

with open(filename) as f:
    reader = csv.reader(f)
    header_now = next(reader)

    for index,column_header in enumerate(header_now):         #enumrate()方法来获取每个元素的索引及其值
        print(index,column_header)
