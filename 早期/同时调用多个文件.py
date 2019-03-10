def count_words(filename):
    """计算一个文件大概包含多少单词"""
filenames = ['All car','programs','your_car','hao.txt']
for filename in filenames:
    count_words(filename)

    try:
        with open(filename) as f_job:
            contents = f_job.read()
    except FileNotFoundError:
        msg = "sorry don‘t has the book "
        print(msg)
    else:
        #计算文件大致包含多少单词
        words = contents.split()
        num_words = len(words)
        print("The file is " + filename + str(num_words) + " words !")

filename = r'C:\Users\13436\PycharmProjects\learnpy\hao.txt'
filename = 'hao.txt'
count_words(filename)

