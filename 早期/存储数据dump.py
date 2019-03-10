#json.dump()和json.load()

import json                         #导入json模块

numbers = [1,3,5,7,9]
filename = 'numbers.json'           #指定了要将数字列表存储到其中的文件的名称
with open(filename,'w') as f_job:   #以写入模式打开文件 json数据能够写入其中
    json.dump(numbers,f_job)        #使用函数json.dump()将数字存储到文件numbers中
