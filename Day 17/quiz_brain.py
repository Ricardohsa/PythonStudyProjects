class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.questions_list = question_bank
        self.score = 0
    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        print(f"{current_question.category} - {current_question.difficulty}")
        user_answer = input(f"Q.{self.question_number}: {current_question.text}True/False?:")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"That's wrong.")

        print(f"The correct answer was: {correct_answer}\nYour current score is "
              f"{self.score}/{self.question_number}")
        print("\n")
