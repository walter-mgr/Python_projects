# # Give a feddback

import random
from termcolor import cprint, colored
import re

EXIT = "q"


class ConstColors:
    COLOR_CYAN = "cyan"
    COLOR_GREEN = "green"
    COLOR_YELLOW = "yellow"
    COLOR_RED = "red"


def get_four_unique_digit_number() -> str:
    digits = random.sample(range(10), 4)
    return "".join([str(digit) for digit in digits])


def is_valid_len(user_input):
    return len(user_input) == 4


def is_all_digits(user_input):
    return str(user_input).isdigit()


def is_four_digit_set(user_input):
    return len(set(user_input)) == 4


def is_four_digit_number(number: str) -> bool:
    pattern = r"^\d{4}$"
    return bool(re.match(pattern, number))


def get_valid_user_input():
    while True:
        user_input = input("Guess (to quit press 'Q'): ").lower().strip()
        if user_input == EXIT:
            return user_input
        if (
            is_four_digit_number(user_input)
            # is_valid_len(user_input)
            # and is_all_digits(user_input)
            # and is_four_digit_set(user_input)
        ):
            return user_input
        cprint("Invalid input", ConstColors.COLOR_RED)


def count_bulls_cows(secret_number, user_guess):
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


def print_feedback(bulls, cows, secret_number):
    print(f"Feedback: {bulls} bulls, {cows} cows")
    if bulls == len(secret_number):
        cprint("\nYou win!", ConstColors.COLOR_GREENs)
        return


def main():
    secret_number = get_four_unique_digit_number()
    print(secret_number)  # remove me after finish
    cprint("Try to guess a 4-digit number with unique digits.", ConstColors.COLOR_CYAN)
    while True:
        user_guess = get_valid_user_input()
        if user_guess == EXIT:
            cprint(
                f"You gave up too soon! Secret number is: {secret_number}",
                ConstColors.COLOR_YELLOW,
            )
            break

        bulls, cows = count_bulls_cows(secret_number, user_guess)
        if secret_number == user_guess:
            print_feedback(bulls, cows, secret_number)
            break

        print_feedback(bulls, cows, secret_number)


if __name__ == "__main__":
    main()


"""

    assert (
        len(get_four_unique_digit_number()) == 4
    ), "Test failed: The result must be 4 digits long"
    assert (
        len(set(get_four_unique_digit_number())) == 4
    ), "Test failed: The digits must be unique"
    assert (
        get_four_unique_digit_number().isdigit()
    ), "Test failed: The result must contain only digits"
    print("All tests passed!")

    TODO: reconsider validation

    def is_four_digit_number(number: str) -> bool:
        pattern = r"^\d{4}$"
        return bool(re.match(pattern, number))

    Explanation:
    1. Pattern r"^\d{4}$":

        ^ : Asserts position at the start of the string.

        \d : Matches any digit (equivalent to [0-9]).

        {4} : Matches exactly 4 digits.

        $ : Asserts position at the end of the string.    

    # Example usage:
    print(is_four_digit_number("1234"))  # True
    print(is_four_digit_number("123"))   # False
    print(is_four_digit_number("abcd"))  # False


    """

"""
command for running tests:
cd / project_dir ->
python -m unittest discover -s tests
"""
