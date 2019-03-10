import csv
filename = (r'C:\Users\13436\PycharmProjects\learnpy\csv_dict_data1.csv')
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)