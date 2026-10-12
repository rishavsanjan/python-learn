import json
class Question:    
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, answer):     
            if self.options[answer - 1] == self.correct_answer:
                print("Correct!")
                return True
            else:
                print("Wrong!")
                return False


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

            if answer < 1 or answer > len(self.options):
                print("Invalid input!")
                continue

            break

        is_correct = self.check_answer(answer)

        return is_correct


score = 0

with open("questions.json", "r") as file:
    questionsFromJSON = json.load(file)

questions = []

for question in questionsFromJSON:
    question_text = question["question_text"]
    options = question["options"]
    correct_answer = question["correct_answer"]
    q = Question(question_text, options, correct_answer)
    questions.append(q)

for question in questions:
    is_correct = question.print_question()
    if is_correct:
        score += 1

print("Your score:", score, "/", len(questions))

