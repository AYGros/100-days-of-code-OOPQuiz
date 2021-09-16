from question_model import Question
from data import question_data

question_bank = []

for dataset in question_data:
    question = Question(dataset["text"], dataset["answer"])
    question_bank.append(question)

print(question_bank)