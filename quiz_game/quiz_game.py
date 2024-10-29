A = "a"
B = "b"
C = "c"
D = "d"


questions = [
    "What is the capital of France?",
    "Which planet is known as the red planet?",
    "What is the largest ocean on Earth?",
]
answers = [
    {"a": "Berlin", "b": "Madrid", "c": "Paris", "d": "Rome", "correct": "c"},
    {"a": "Earth", "b": "Mars", "c": "Jupiter", "d": "Saturn", "correct": "b"},
    {"a": "Atlantic", "b": "Indian", "c": "Arctic", "d": "Pacific", "correct": "d"},
]

answer_options = (A, B, C, D)


def counter():
    count = -1

    def increase_by_one(value=1) -> int:
        nonlocal count
        count += value
        return count

    return increase_by_one


question_index = counter()
correct_answer_index = counter()
user_answer_index = counter()
correct_answers_count = counter()


def put_question(question_index, answer):

    question = f"""
Question {question_index + 1}: {questions[question_index]}
A. {answers[answer]["a"]}
B. {answers[answer]["b"]}
C. {answers[answer]["c"]}
D. {answers[answer]["d"]}"""
    print(question)


def get_user_answer():
    while True:
        user_answer = input("Your answer: ").lower().strip()
        if user_answer in answer_options:
            return user_answer
        else:
            print("Please select from the next options: (A/B/C/D)")


def display_answers(user_answer_index: int, user_answer: str):
    correct_answer = answers[user_answer_index]["correct"]

    if user_answer == correct_answer:
        correct_answers_count()
        print(f"Correct!")

    else:
        print(f"Wrong answer! Correct answer is {correct_answer.upper()}")


def main():
    while True:
        try:
            put_question(question_index(), correct_answer_index())
            user_answer = get_user_answer()
            display_answers(user_answer_index(), user_answer)

        except:
            break
    print(
        f"Quiz over! Your final score is {correct_answers_count()} of {len(questions)}"
    )


if __name__ == "__main__":
    main()
