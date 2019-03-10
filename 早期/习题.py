
import json
fum = 'number.json'
try:
    with open(fum) as f_d:
        number = json.load(f_d)
except FileNotFoundError:
    number = input("请输入一个数字: " )
    with open(number,'w') as f_d:
        json.dump(number,f_d)
        print("ojbk")
else:
    print("I know you favrite numbei is " + number)