class Notebook():
    """收集匿名信"""
    def __init__(self,question,new_responses):
        self.question = question
        self.responses = []
        self.new_responses = new_responses
    @property

    def show_question(self,question):
        """显示问卷"""
        print(question)

    def store_question(self,new_response):
        """新增并存储问卷"""
        self.responses.append(new_response)

    def show_results(self,responses):
        """展示所有问卷的答案"""
        print("Survey results:")
        for response in responses:
            print('- ' +response)