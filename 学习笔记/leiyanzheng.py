from testlei import Wenjuan

question = "你最喜欢的语言是什么？？？"
my_question = Wenjuan(question)

my_question.show_question()
print("Enter q to quit\n")
print("预计有")
while True:
    answers = input("语言是：")
    if answers == 'q':
        break
    my_question.tj_answer(answers)
    print(answers)

print("以上是全部内容")
my_question.show_all_quertion()
