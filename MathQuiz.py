import random

score = 0  # Initialize score before the loop
total_questions = 0
quiz_history = []

# Instructions
a = input("Welcome to math trivia. Would you like to play? (y/n): ")

if a.lower() == 'n':
    print("Well, bye then.")
elif a.lower() == 'y':
    f = int(input('How many questions would you like to answer? '))
    total_questions = f
    print("Here are the instructions:")
    print("You will start with 0 points. Each time you get a question right, you will get 1 point added to your score.")
    print('first question:')

    # Asking questions
    for x in range(f):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        question = "What is {0} + {1}? ".format(num1, num2)
        answer = int(input(question))

        # Checking the answer
        if answer == (num1 + num2):
            print("Correct!")
            score += 1
            is_correct = True
        else:
            print("Incorrect. The correct answer is", (num1 + num2))
            is_correct = False

        # Adding question to quiz history
        quiz_history.append({
            "question": question,
            "user_answer": answer,
            "correct_answer": num1 + num2,
            "is_correct": is_correct
        })

        print("Score:", score, "/", total_questions)

    # Summary of the score
    percentage = (score / total_questions) * 100
    print("You completed the math quiz. Your final score is", score, "/", total_questions)
    print("Your percentage is {:.2f}%".format(percentage))

    # Displaying quiz history
    print("\nQuiz History:")
    for idx, qh in enumerate(quiz_history, start=1):
        print(f"Question {idx}:")
        print("Question:", qh["question"])
        print("Your Answer:", qh["user_answer"])
        print("Correct Answer:", qh["correct_answer"])
        print("Result:", "Correct" if qh["is_correct"] else "Incorrect")
        print()
else:
    print("Well, bye then.")








