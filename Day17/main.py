from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []


def import_questions():
    for question in question_data:
        answers = []
        for values in question.items():
            (text, answer) = values
            answers.append(answer)
        questions.append(Question(answers[0], answers[1]))


def run_quiz():
    import_questions()
    test_quiz = QuizBrain(questions)

    while test_quiz.still_has_questions():
        question = test_quiz.next_question()
        question_text = question.text
        answer = question.answer
        user_answer = input(f"Q.{test_quiz.question_number}: {question_text} (True/False)?: ")
        test_quiz.update_score(user_answer, answer)
        test_quiz.print_current_score()
    print("You've completed the quiz.")
    print(f"Your final score is {test_quiz.score}/{test_quiz.question_number}")


if __name__ == '__main__':
    run_quiz()
