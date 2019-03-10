from server import Notebook
#定义一个温蒂，并创建一个表示调查的Notebook对象


question = "What 's your favrouite language ???"
my_server = Notebook(question, new_responses)


#显示问题并存储答案
my_server.show_question(question)
print("Enter 'w' to quit .\n ")
while True:
    response = input("Language: ")
    if response == 'w':
        break
    my_server.store_question(response)



#显示调查结果
print("\n Thank your very much !!!")
my_server.show_results()
