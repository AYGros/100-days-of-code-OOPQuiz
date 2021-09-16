from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dataset in question_data:
    question = Question(dataset["question"], dataset["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz")
print(f"Your final score is {quiz.score}/{len(question_bank)}")