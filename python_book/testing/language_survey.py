from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language you learned first?"
language_survey = AnonymousSurvey(question)

# Show the question, and store responses to the sruvey.
language_survey.show_question()
print("Enter 'q' to quit the survey.")
while True:
    response = input("\tLanguage: ")
    if response == "q":
        break
    language_survey.store_response(response)

# Show  the survey results
print("\nThank you for taking the survey! <3")
language_survey.show_responses()
