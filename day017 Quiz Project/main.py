from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# convert the question data (which is in dict format) to objects
question_bank = []
for ques in question_data:
    ques_text = ques["question"]
    ques_ans = ques["correct_answer"]
    question_bank.append(Question(ques_text, ques_ans))

quiz = QuizBrain(question_bank)
while quiz.is_there_next_question():
    quiz.ask_question()

print("You have completed the quiz!!")
print(f"Here's your final score : {quiz.score}/{len(question_bank)}")
