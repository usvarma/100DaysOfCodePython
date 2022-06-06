import random


class QuizBrain:
    """Main class controlling the quiz"""

    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.question_list = questions

    def next_question(self):
        self.question_number += 1
        return self.question_list[self.question_number - 1]

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def update_score(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score += 1
            print("Your answer was correct")
        else:
            print(f"Incorrect answer. Correct answer was {answer}")

    def print_current_score(self):
        print(f"Your current score is {self.score}/{self.question_number}")

