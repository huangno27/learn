from name_fun import get_formatted_name
print("Enter q to quit")
while True:
    first = input("\n请输入你的姓")
    if first == 'q':
        break
    middle = input("\n请输入你的小名")
    if middle == 'q':
            break
    last = input("\n请输入你的名")
    if last == 'q':
     break

    for_name = get_formatted_name(first ,last, middle)
    print("\n" + for_name + " drop the beat")
    break