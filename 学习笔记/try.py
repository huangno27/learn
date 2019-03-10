filename = (r'F:\liucheng.txt')

try:
    with open(filename) as f_job:
        contents = f_job.read()
        print("yes")
except FileExistsError:
    print("没有找到" + filename)
else:
    word = contents.split()
    new_word = len(contents)
    print(filename + " 有 " + str(new_word) + " 个字!")
