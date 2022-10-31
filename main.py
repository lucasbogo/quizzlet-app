from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = [] # question bank = a list of question objects | Emptylist = []

for question in question_data: # Loop through each of the questins inside the question_data
    question_text = question["text"] # for each of this questions, I created a variable called question_text
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer) # this constructor expects two parameters
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)
quiz.next_question()