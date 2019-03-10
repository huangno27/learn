class Notebook:
    def quesyion(self,question):
        """存储一个问题的答卷"""
        self.quesyion = question
        self.responses = []

    def show_question(self):
        """展示答卷"""
        print(self.question)

    def store_question(self,new_responses):
        """存储单份答卷"""
        self.new_responses.append(new_responses)

    def show_answer(self):
        """显示所有答卷"""
        print("所有答卷：")
        for response in self.responses:
            print("_" + response)