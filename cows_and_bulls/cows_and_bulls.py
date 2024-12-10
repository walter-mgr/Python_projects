import random
from termcolor import cprint
import re


class ConstMenuOptions:
    EXIT = "q"
    GET_HINT = "h"


class ConstColors:
    COLOR_CYAN = "cyan"
    COLOR_GREEN = "green"
    COLOR_YELLOW = "yellow"
    COLOR_RED = "red"


def get_four_unique_digit_number() -> str:
    digits = random.sample(range(10), 4)
    return "".join([str(digit) for digit in digits])


def is_four_digit_number(user_input: str) -> bool:
    pattern = r"^\d{4}$"
    return bool(re.match(pattern, user_input))


def is_four_digit_set(user_input: str) -> bool:
    return len(set(user_input)) == 4


def get_valid_user_input() -> str:
    while True:
        user_input = input("Guess (to quit press 'Q'): ").lower().strip()
        if (
            user_input == ConstMenuOptions.EXIT
            or user_input == ConstMenuOptions.GET_HINT
        ):
            return user_input
        if is_four_digit_number(user_input) and is_four_digit_set(user_input):
            return user_input
        cprint("Invalid input", ConstColors.COLOR_RED)


def count_bulls_cows(secret_number: str, user_guess: str) -> tuple:
    bulls = len(
        [
            digit
            for index, digit in enumerate(secret_number)
            if user_guess[index].__eq__(secret_number[index])
        ]
    )
    cows = len([digit for digit in user_guess if digit in secret_number])
    if bulls:
        cows -= bulls

    return bulls, cows


def get_random_hint(secret_number, num_replace=3, replace_to="_"):
    hint_sequence = list(secret_number)
    positions = random.sample(range(len(hint_sequence)), num_replace)
    for position in positions:
        hint_sequence[position] = replace_to
    return "".join(hint_sequence)


def print_feedback(bulls, cows, secret_number, attempts):
    cprint(f"Feedback: {bulls} bulls, {cows} cows", ConstColors.COLOR_CYAN)
    if bulls == len(secret_number):
        cprint(f"\nThe number was: {secret_number}", ConstColors.COLOR_YELLOW)
        cprint(f"\nYou win! You had {attempts} tries.", ConstColors.COLOR_GREEN)
        return


def main():
    secret_number = get_four_unique_digit_number()
    attempts = 0
    cprint(
        "\nTry to guess a 4-digit number with unique digits.", ConstColors.COLOR_CYAN
    )

    while True:
        user_guess = get_valid_user_input()

        if user_guess == ConstMenuOptions.EXIT:
            cprint(
                f"You gave up too soon! Secret number is: {secret_number}",
                ConstColors.COLOR_YELLOW,
            )
            break
        if user_guess == ConstMenuOptions.GET_HINT:
            hint = get_random_hint(secret_number)
            cprint(f"Here is a hint: {hint} ", ConstColors.COLOR_YELLOW)
            continue

        bulls, cows = count_bulls_cows(secret_number, user_guess)
        attempts += 1

        if secret_number == user_guess:
            print_feedback(bulls, cows, secret_number, attempts)
            break

        print_feedback(bulls, cows, secret_number, attempts)


if __name__ == "__main__":
    main()
