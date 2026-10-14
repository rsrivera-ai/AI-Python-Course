# AC 4.3 - Using the Python standard library random module
import random

question1 = {
    "question": "In what year was the Battle of Waterloo fought?",
    "choices": ["A. 1805", "B. 1812", "C. 1815", "D. 1821"],
    "answer": "C"
}

question2 = {
    "question": "Which French Marshal led the major cavalry charges against the Allied centre at the Battle of Waterloo?",
    "choices": ["A. Marshal Ney", "B. Marshal Murat", "C. Marshal Grouchy", "D. Marshal Davout"],
    "answer": "A"
}

question3 = {
    "question": "Which Prussian commander’s arrival was crucial in helping defeat Napoleon at the Battle of Waterloo?",
    "choices": ["A. Gebhard Leberecht von Blücher", "B. Karl von Bülow", "C. August von Gneisenau", "D. Friedrich Wilhelm III"],
    "answer": "A"
}

questions = [question1, question2, question3]

# AC 3.1 - User-defined function containing a series of commands

def get_valid_answer():
    answer = input("Enter A, B, C or D: ").upper()

    while answer not in ["A", "B", "C", "D"]:
        print("Invalid answer. Please try again.")
        answer = input("Enter A, B, C or D: ").upper()

    return answer


def runquiz():
    score = 0

    # AC 4.3 - Use random module to shuffle question order
    random.shuffle(questions)

    # AC 2.3 - For loop repeats the quiz for each question
    for question in questions:
        print(question["question"])

        # AC 2.3 - For loop repeats each answer choice
        for choice in question["choices"]:
            print(choice)

        # Refactoring: call the reusable input-validation function
        answer = get_valid_answer()

        # AC 2.1 - Decision-making using if/else
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")

    # AC 2.2 - len() and print() are built-in functions
    print("Your score is:", score, "out of", len(questions))

# AC 4.1 - Run the completed Python script
runquiz()