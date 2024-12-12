""" Password Strength Checker

This program evaluates the strength of a given password based on predefined criteria:
1. Very Weak
2. Weak
3. Medium
4. Strong
5. Very Strong

The program uses regex patterns to assess the password strength and categorizes
it accordingly.

Password Strength Criteria:
- Very Weak: 4 digits
- Weak: 8 digits
- Medium: 6 characters with at least one uppercase letter
- Strong: More than 7 characters with at least one uppercase and one lowercase letter
- Very Strong: More than 8 characters with at least one uppercase letter, one
    lowercase letter, and at least one special symbol

User Input:
- The user is prompted to enter a password or quit the programm.
- The program then evaluates and prints the strength of the password.

Functions:
- check_password_strength(password: str, strength_criteria: dict) -> str: Evaluates
    the strength of the given password based on predefined regex patterns.
- get_valid_user_input() -> str: Prompts the user to enter a password and ensures it
    meets the minimum length requirement, and also prompts the user to quit the programm.
- print_color(strong_pass: str) -> str: Determines the color associated with the password
    strength level.
- main(): The main function that runs the password strength checker. Prompts the user
    for a password, evaluates its strength, and provides feedback.

"""

import re
from termcolor import cprint, colored


class ConstCommands:
    QUIT = "q"


class ConstColors:
    COLOR_CYAN = "cyan"
    COLOR_YELLOW = "yellow"
    COLOR_GREEN = "green"
    COLOR_RED = "red"
    COLOR_LIGHT_MAGENTA = "light_magenta"


class ConstStrongCriteria:
    VERY_STRONG = "Very Strong"
    STRONG = "Strong"
    MEDIUM = "Medium"
    WEAK = "Weak"
    VERY_WEAK = "Very Weak"


strength_criteria = {
    ConstStrongCriteria.VERY_STRONG: r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*(),.?:{}|<>]).{8,}$",
    ConstStrongCriteria.STRONG: r"^(?=.*[A-Z])(?=.*[a-z]).{7,}$",
    ConstStrongCriteria.MEDIUM: r"^(?=.*[A-Z]).{6,}$",
    ConstStrongCriteria.WEAK: r"^\d{8}$",
    ConstStrongCriteria.VERY_WEAK: r"^\d{4}$",
}


def check_password_strength(password: str, strength_criteria: dict) -> str:
    """Evaluates the strength of the given password based on predefined regex patterns."""
    for strength, pattern in strength_criteria.items():
        if re.match(pattern, password):
            return strength
    return "Very Weak"


def get_valid_user_input() -> str:
    """Prompts the user to enter a password and ensures it meets the minimum length
    1requirement."""
    while True:
        user_input = input(
            colored(
                "\nEnter a password (or press 'q' to quit): ", ConstColors.COLOR_CYAN
            )
        ).strip()

        if user_input == ConstCommands.QUIT or len(user_input) >= 4:
            return user_input
        cprint(
            "Password is too short. Please enter at least 4 characters",
            ConstColors.COLOR_RED,
        )


def print_color(strong_pass: str) -> str:
    """Determines the color associated with the password strength level."""
    color = {
        ConstStrongCriteria.VERY_STRONG: ConstColors.COLOR_GREEN,
        ConstStrongCriteria.STRONG: ConstColors.COLOR_CYAN,
        ConstStrongCriteria.MEDIUM: ConstColors.COLOR_YELLOW,
        ConstStrongCriteria.WEAK: ConstColors.COLOR_LIGHT_MAGENTA,
        ConstStrongCriteria.VERY_WEAK: ConstColors.COLOR_RED,
    }[strong_pass]
    return color


def main():
    """The main function that runs the password strength checker. It prompts the user
    for a password, evaluates its strength, and provides feedback."""
    while True:
        password = get_valid_user_input()

        if password == ConstCommands.QUIT:
            break

        strong_pass = check_password_strength(password, strength_criteria)

        color = print_color(strong_pass)

        cprint(f"Your password is {strong_pass}", color)

        if strong_pass == ConstStrongCriteria.VERY_STRONG:
            break


if __name__ == "__main__":
    main()
