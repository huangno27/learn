filename = r'C:\Users\acer\PycharmProjects\learn\book.txt'
with open(filename,'w') as file_name:                                     #r 读取 w 写入 a 附加 读取和写入同时 r+
    file_name.write("I Love My People !\n")
    file_name.write("v.\n")
    file_name.write("ddsk.\n")

filename = r'C:\Users\acer\PycharmProjects\learn\book.txt'
with open(filename,'a') as fild_name:
    fild_name.write("bitch is a bitch.\n")
    fild_name.write("so what ?")
