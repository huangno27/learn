from cc import AnoymousSurvey
question = "what are you like ?"
my_survey = AnoymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at anytime to quit ")
while True:
    response = input("language: ")
    if response == 'q':
        break
    my_survey.store_question(response)

print("thank you very much")
my_survey.show_results()