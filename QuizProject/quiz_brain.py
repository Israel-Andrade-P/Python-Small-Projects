class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        u_answer = input(f"Q.{self.question_number}: {question.text} True/False? ").title()
        self.check_answer(u_answer, question.answer)
           
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score+= 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.question_number}")   
        print("\n")        

    def still_has_questions(self):
        return self.question_number != len(self.question_list)
