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


