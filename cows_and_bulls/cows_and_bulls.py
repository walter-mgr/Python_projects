"""
COWS AND BULLS GAME

Objective:
Develop a text-based implementation of the "Cows and Bulls" game where
the player guesses a secret 4-digit number with unique digits. The game provides
feedback on each guess in terms of "bulls" (correct digits in the correct positions)
and "cows" (correct digits in the wrong positions). The player can also request
hints or exit the game.

Classes:
- ConstMenuOptions: Holds menu options for exiting and getting hints.
- ConstColors: Contains color constants for output.
- GameConfig: Stores game configuration constants like the number of digits.

Functions:
- get_four_unique_digit_number: Generates a random 4-digit number with unique digits.
- is_four_digit_number: Validates if the input is a 4-digit number.
- is_four_digit_set: Validates if the input consists of 4 unique digits.
- get_valid_user_input: Prompts the user for a valid 4-digit guess or an exit command.
- count_bulls_cows: Counts the number of bulls and cows in the user's guess.
- get_random_hint: Generates a hint by replacing random digits in the secret number
    with a given character.
- print_feedback: Provides feedback on the user's guess, including the number of bulls
    and cows.
- main: The main game loop that handles user interaction and game flow.

Game Flow:
1. Generate a secret 4-digit number with unique digits.
2. Prompt the player to enter a guess, request a hint, or exit the game.
3. Validate the user's input to ensure it's a valid 4-digit number with unique digits.
4. Provide feedback on the guess in terms of bulls and cows.
5. If requested, provide a hint by revealing a specified number of digits in the
    secret number.
6. Track the number of attempts made by the player.
7. Continue the game loop until the player guesses the secret number correctly
    or chooses to exit.

"""

import random
from termcolor import cprint
import re


class ConstMenuOptions:
    """Class to hold menu options."""

    EXIT = "q"
    GET_HINT = "h"


class ConstColors:
    """Class to hold color constants for output."""

    COLOR_CYAN = "cyan"
    COLOR_GREEN = "green"
    COLOR_YELLOW = "yellow"
    COLOR_RED = "red"


class ConstNumberConfig:
    """Class to hold game configuration constants."""

    NUMBER_LENGTH = 4


def get_four_unique_digit_number() -> str:
    """Generate a 4-digit number with unique digits."""
    digits = random.sample(range(10), ConstNumberConfig.NUMBER_LENGTH)
    return "".join([str(digit) for digit in digits])


def is_four_digit_number(user_input: str) -> bool:
    """Check if the input is a 4-digit number."""
    pattern = r"^\d{4}$"
    return bool(re.match(pattern, user_input))


def is_four_digit_set(user_input: str) -> bool:
    """Check if the input is a 4-digit number."""
    return len(set(user_input)) == ConstNumberConfig.NUMBER_LENGTH


def get_valid_user_input() -> str:
    """Prompt the user for a valid 4-digit guess or an exit command."""
    while True:
        user_input = (
            input("Guess (to quit press 'Q', for a hint press 'H'): ").lower().strip()
        )
        if (
            user_input == ConstMenuOptions.EXIT
            or user_input == ConstMenuOptions.GET_HINT
        ):
            return user_input
        if is_four_digit_number(user_input) and is_four_digit_set(user_input):
            return user_input
        cprint(
            "Please enter a 4-digit number with unique digits", ConstColors.COLOR_RED
        )


def count_bulls_cows(secret_number: str, user_guess: str) -> tuple:
    """Count the number of bulls and cows in the user guess."""
    bulls = len(
        [
            digit
            for index, digit in enumerate(secret_number)
            if user_guess[index].__eq__(secret_number[index])
        ]
    )
    cows = len([digit for digit in user_guess if digit in secret_number]) - bulls

    return bulls, cows


def get_random_hint(
    secret_number: str, num_replace: int = 3, replace_to: str = "_"
) -> str:
    """Generate a hint for the secret number by randomly selecting a number of
    positions and replacing the digits at those positions with a given character."""
    hint_sequence = list(secret_number)
    positions = random.sample(range(len(hint_sequence)), num_replace)
    for position in positions:
        hint_sequence[position] = replace_to
    return "".join(hint_sequence)


def print_feedback(bulls: int, cows: int, secret_number: str, attempts: int) -> None:
    """Print feedback on the user's guess."""
    cprint(f"Feedback: {bulls} bulls, {cows} cows", ConstColors.COLOR_CYAN)
    if bulls == len(secret_number):
        cprint(f"\nThe number was: {secret_number}", ConstColors.COLOR_YELLOW)
        cprint(f"\nYou win! You had {attempts} tries.", ConstColors.COLOR_GREEN)
        return


def main():
    """Main function to run the game."""
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
