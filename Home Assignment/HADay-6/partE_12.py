# 12.Build a Mini Quiz Game using Functions
# Use a function ask_question(question, correct_answer)
# Ask 3–5 questions and return score at the end
def ask_question(question, correct_answer):
    user_answer = input(question + " ")
    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!\n")
        return 1
    else:
        print(f"Wrong! The correct answer is {correct_answer}.\n")
        return 0

def run_quiz():
    score = 0
    print("Welcome to the Quiz Game!\n")

    score += ask_question("What is the capital of India?", "New Delhi")
    score += ask_question("What planet is known as the Red Planet?", "Mars")
    score += ask_question("What is the square root of 64?", "8")
    score += ask_question("What is your name:","Sumedh")
    score += ask_question("What is the chemical symbol for water?", "H2O")

    print(f"Your final score is {score}/5")

run_quiz()