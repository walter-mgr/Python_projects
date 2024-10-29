from termcolor import cprint
import random

QUESTION = "question"
OPTIONS = "options"
CORRECT = "correct"

quiz = [
    {
        QUESTION: "What is the capital of France?",
        OPTIONS: [
            "A. Berlin",
            "B. Madrid",
            "C. Paris",
            "D. Rome",
        ],
        CORRECT: "c",
    },
    {
        QUESTION: "Which planet is known as the red planet?",
        OPTIONS: [
            "A. Earth",
            "B. Mars",
            "C. Jupiter",
            "D. Saturn",
        ],
        CORRECT: "b",
    },
    {
        QUESTION: "What is the largest ocean on Earth?",
        OPTIONS: [
            "A. Atlantic",
            "B. Indian",
            "C. Arctic",
            "D. Pacific",
        ],
        CORRECT: "d",
    },
]


def ask_question(index, question, options):
    print(f"Question {index}: {question}")
    for option in options:
        print(option)


def get_user_answer():
    options = ("a", "b", "c", "d")
    while True:
        user_answer = input("Your answer: ").lower().strip()
        if user_answer in options:
            return user_answer
        else:
            cprint("Select from the next options: (A/B/C/D)", "yellow", "on_grey")


def run_quiz():
    random.shuffle(quiz)
    score = 0

    for index, question in enumerate(quiz, 1):
        ask_question(index, question[QUESTION], question[OPTIONS])

        user_answer = get_user_answer()

        if user_answer == question[CORRECT]:
            cprint(
                """Correct!
                   """,
                "green",
            )
            score += 1
        else:
            cprint(
                f"""Wrong! Correct answer is {question[CORRECT].upper()}
                """,
                "red",
            )

    cprint(f"Quiz over! Your total score is {score} of {len(quiz)}", "light_cyan")


if __name__ == "__main__":
    run_quiz()
