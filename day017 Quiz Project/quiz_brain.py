# todo: asking the user questions

# todo: checking if the answer was right

# todo: checking whether we are at the end of the question bank. if true: we stop the game

class QuizBrain:
    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list
        self.score = 0

    def ask_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1  # incrementing here is beneficial since, below we get the
        # actual Q__ number printed (in a 0 indexed list the question number starts from 0)
        user_answer = input(f"Q{self.question_number}. {current_question.text}? (true/false)")

        self.check_answer(user_answer, current_question.answer)

    def is_there_next_question(self):
        """returns True if there is a next question. returns False if we are at the last question"""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, actual_answer):
        if user_answer.lower().strip() == actual_answer.lower().strip():
            self.score += 1
            print("You have guessed it right!")
        else:
            print("Sorry! You're guess is incorrect")
        print(f"The correct answer was {actual_answer}")
        print(f"The current score is : {self.score}/{self.question_number}\n")


