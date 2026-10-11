score = 0
class Question:
    
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, answer):     
            if self.options[answer - 1] == self.correct_answer:
                print("Correct!")
                self.score += 1
            else:
                print("Wrong!")


    def print_question(self):
        print(self.question_text)

        for index, option in enumerate(self.options, start=1):
            print(index, ". ", option)

        while True:
            try:
                answer = int(input("Enter your answer : "))
            except ValueError:
                print("Invalid input!")
                continue    

            if answer < 1 or answer > 4:
                print("Invalid input!")
                continue

            break

        self.check_answer(answer)

    def print_score(self):
        print("The score is ", self.score, "/3")

q1 = Question("Where is the capital of India ? ", ["Mumbai", "New Delhi", "Indore", "Kolkata"], "New Delhi")
q1.print_question()
q1 = Question("Where is the capital of Maharashtra ? ", ["Pune", "Thane", "Vadodra", "Mumbai"], "Mumbai")
q1.print_question()
q1 = Question("Where is the capital of Madhya Pardesh ? ", ["Bhopal", "Indore", "Jabalpur", "Sagar"], "Bhopal")

q1.print_question()

q1.print_score()
