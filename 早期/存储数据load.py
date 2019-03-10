import json
filename = 'numbers.json'
with open(filename,'r') as f_job:  #读取之前写入的文件
    numbers = json.load(f_job)     #加载存储在numbers.json中的信息，并将其存储到numbers中

print(numbers)

