class AnonymousSurvey:
    def __init__(self, question):
        """Store a question and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response of the survey."""
        self.responses.append(new_response)

    def show_responses(self):
        """Show responses to the survey."""
        print("Survey results: ")
        for response in self.responses:
            print(f"\t- {response}")