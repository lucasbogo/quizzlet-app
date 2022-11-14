from question_model import Question
from data import question_data
from quiz_factory import QuizFactory
from ui import QuizInterface


question_bank = [] # question bank = a list of question objects | Emptylist = []

for question in question_data: # Loop through each of the questins inside the question_data.
    question_text = question["question"] # for each of this questions, I created a variable called question_text.
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer) # this constructor expects two parameters.
    question_bank.append(new_question)

# Create question bank
quiz = QuizFactory(question_bank)
# Create Quiz Interface
quiz_ui = QuizInterface()

# Check if the quiz still has questions through a while loop | commented this, because TKinter might get confused as it runs in a While Loop by default
""" while quiz.still_has_questions():
    # If True: there are questions, then go to next one. If False, closes the while loop.
    quiz.next_question() """

print(f"You've completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")