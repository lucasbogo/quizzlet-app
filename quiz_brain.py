# asking the questions
# checking if the answer was correct
# checking if we're the end of the quiz

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0 # Attribute with default value 0;
        self.question_list = q_list
        
    # Method to check if there are still questions left. This will be called in the 'While Loop' in main.py
    def still_has_questions(self):
        # len function: Gets the lenght of question_list
        # If Condition: Check for end of list. If the number of questions is less than the question list, Return True,
        if self.question_number < len(self.question_list):
            return True
        # Otherwise, return False
        else:
            False 
    
    # Method NextQuestion
    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number}:{current_question.text} (True/False): ")