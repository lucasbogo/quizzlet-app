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
quiz_ui = QuizInterface(quiz) # the quiz that is created from the quiz_factory is passed inside the UI. To chatch it, i added a paramenter in the init of the UI
