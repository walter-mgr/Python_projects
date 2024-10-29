from random import randint


secret_number = randint(1, 100)


def counter():
    count = []

    def counter(value=1) -> int:

        count.append(value)
        return sum(count)

    return counter


attempts = counter()

while True:

    try:
        guessed_number = int(input("Guess the number between 1 and 100: "))
        attempts()

        if guessed_number < secret_number:
            print("Too low!")
        elif guessed_number > secret_number:
            print("Too high!")
        else:
            print(
                f"""
  Congratulations! You guessed the number! {guessed_number}
  You had {attempts()} attempts"""
            )
            break

    except ValueError:
        print("Wrong input! Please enter a valid number )))")
