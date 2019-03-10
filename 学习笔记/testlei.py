class Wenjuan():
    def __init__(self,question):
        self.question = question
        self.answers = []

    def show_question(self):
        """展示问卷内容"""
        print(self.question)


    def tj_answer(self,new_answer):
        """存储并添加答案"""
        self.answers.append(new_answer)

    def show_all_quertion(self):
        print("所有答案")
        for answer in self.answers:
            print(answer)
