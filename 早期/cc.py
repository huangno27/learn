class AnoymousSurvey():
    """收集匿名信"""
    def __init__(self,question):
        self.question = question
        self.responses = []

    def show_question(self):
        """显示问卷"""
        print(self.question)

    def store_question(self,new_response):
        """新增并存储问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """展示所有问卷的答案"""
        print("Survey results:")
        for response in self.responses:
            print('- ' +response)