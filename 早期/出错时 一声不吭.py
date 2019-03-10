def count_words(filename):
    """计算一个文件大致包含多少单词"""
    try:
        with open(filename) as f_job:
            contents = f_job.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file is " + filename + str(num_words) + " words !")

filenames = ['All car','programs','your_car','hao.txt']
for filename in filenames:
    count_words(filename)


#当py出错时 不要报出来 给用户看到
