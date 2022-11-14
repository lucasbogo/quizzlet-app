# asking the questions
# checking if the answer was correct
# checking if we're the end of the quiz

import html # HTML Module for unescaping HTML Entities

class QuizFactory:

    def __init__(self, q_list):
        self.question_number = 0 # Attribute with default value 0;
        self.question_list = q_list
        self.score = 0 # Attribute to keep record of user's right answers;
        
    # Method to check if there are still questions left. This will be called in the 'While Loop' in main.py
    def still_has_questions(self):
        # len function: Gets the lenght of question_list
        return self.question_number < len(self.question_list) # This is the same as the if condition in line 17
    
        # If Condition: Check for end of list. If the number of questions is less than the question list, Return True,
        """  if self.question_number < len(self.question_list):
            return True
        # Otherwise, return False
        else:
            False """ 
    
    # Method NextQuestion
    def next_question(self):
        self.current_question = self.question_list[self.question_number] # Starts off at zero.
        # This ensures that question number gets increased everytime we show the user
        self.question_number += 1
        # Unescape Html entities
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}:{q_text}"
        # Save the user's input inside user_answer variable
        # user_answer = input(f"Q.{self.question_number}:{q_text} (True/False): ")
        # Call check_answer method and pass over the user's answer and correct answer (current_question) within the method
        # self.check_answer(user_answer, current_question.answer)
       
        
    # Method to check if answer is correct or not through users input. It receives user_answer and correct answer to check question
    def check_answer(self, user_answer, correct_answer):
        # Condition: if user's answer is equal to the correct answer | drop to lower case to make comparison easier (True or true, False or false)
        if user_answer.lower() == correct_answer.lower():
            # Increment user score if he or she gets it right
            self.score += 1
            # If it matches the correct answer, print: Right answer!
            print("Right Answer! Great job.")
        else:
            print("Wrong Answer. Dont give up. Keep trying!")
            print(f"The correct answer was: {correct_answer}.")
        # Print user's score out of possible question numbers
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")