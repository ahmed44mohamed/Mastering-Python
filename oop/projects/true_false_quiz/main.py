# Importing section
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions_bank = []

for item in question_data:
    new_q = Question (q_text= item ["question"], q_answer= item ["correct_answer"])
    questions_bank.append (new_q)

quiz = QuizBrain (questions_bank)


while quiz.still_has_questions ():
    quiz.next_question ()


print (f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}")

