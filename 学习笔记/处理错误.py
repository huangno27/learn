file = (r'C:\Users\13436\PycharmProjects\learnpy\All car.py')
try:
    with open(file,encoding="utf-8") as new_wenb:
        second_wenb = new_wenb.read()
except FileNotFoundError:
    msg = "sorry don‘t has the book "
    print(msg)
else:
    words = second_wenb.split()
    new_words = len(words)
    print("The book has " + str(new_words))

def count_words(filename):
    """计算一个文件大概包含多少单词"""
    try:
        with open(filename) as f_job:
            contents = f_job.read()
    except FileNotFoundError:
        msg = "sorry don‘t has the book "
    print(msg)
filename = r'C:\Users\13436\PycharmProjects\learnpy\All car.py'
count_words(filename)
