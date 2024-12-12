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
- Medium: 5 digits with at least one uppercase letter
- Strong: More than 5 digits with at least one uppercase and one lowercase letter
- Very Strong: More than 5 characters with at least one uppercase letter, one lowercase letter, and at least one special symbol

User Input:
- The user is prompted to enter a password.
- The program then evaluates and prints the strength of the password.

"""

import re
from termcolor import cprint, colored


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
    ConstStrongCriteria.VERY_STRONG: r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*(),.?:{}|<>]).{5,}$",
    ConstStrongCriteria.STRONG: r"^(?=.*[A-Z])(?=.*[a-z]).{5,}$",
    ConstStrongCriteria.MEDIUM: r"^(?=.*[A-Z]).{5,}$",
    ConstStrongCriteria.WEAK: r"^\d{8}$",
    ConstStrongCriteria.VERY_WEAK: r"^\d{4}$",
}


def check_password_strength(password: str, strength_criteria: dict) -> str:
    for strength, pattern in strength_criteria.items():
        if re.match(pattern, password):
            return strength
    return "Very Weak"


def get_valid_user_input():
    while True:
        user_input = input(
            colored("\nEnter a password: ", ConstColors.COLOR_CYAN)
        ).strip()
        if len(user_input) >= 4:
            return user_input
        cprint(
            "Password is too short. Please enter at least 4 characters",
            ConstColors.COLOR_RED,
        )


def print_color(strong_pass):

    color = {
        ConstStrongCriteria.VERY_STRONG: ConstColors.COLOR_GREEN,
        ConstStrongCriteria.STRONG: ConstColors.COLOR_GREEN,
        ConstStrongCriteria.MEDIUM: ConstColors.COLOR_YELLOW,
        ConstStrongCriteria.WEAK: ConstColors.COLOR_LIGHT_MAGENTA,
        ConstStrongCriteria.VERY_WEAK: ConstColors.COLOR_RED,
    }[strong_pass]
    return color


def main():
    while True:
        password = get_valid_user_input()

        strong_pass = check_password_strength(password, strength_criteria)

        color = print_color(strong_pass)

        cprint(f"Your password is {strong_pass}", color)

        if strong_pass == ConstStrongCriteria.VERY_STRONG:
            break


if __name__ == "__main__":
    main()
