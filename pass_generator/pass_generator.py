""" Password Generator Program

    This program generates a random password  with unique characters based on
user-defined configurations. The user can specify the length of the password
and choose to include uppercase letters, numbers, and special characters.
The program ensures that the generated password meets the specified criteria.

Project Description:
1. **User Input**: The user is prompted to enter the desired password length
    (minimum 4 characters).
2. **Configuration Options**: The user can choose to include uppercase letters,
    numbers, and special characters.
3. **Character Sequences**: Based on the user's selections, the appropriate
    character sequences are combined.
4. **Password Generation**: A random password is generated from the selected
    character sequences, ensuring it meets the minimum criteria (at least one lowercase
    letter, one uppercase letter, one digit, and one special character).
5. **Output**: The generated password is displayed to the user.

Functions:
- get_pass_length() -> int: Prompts the user to enter the password length.
- get_settings() -> dict: Prompts the user to choose password configurations.
- get_sequence(char_sequences: dict, settings: dict) -> tuple: Returns the character
    sequence based on the user's settings and the corresponding pattern for validation.
- generate_password(sequence: str, length: int, pattern: str) -> str: Generates a random
    password based on the user's configurations and ensures it meets the criteria.
- validate_password(password: str, pattern: str) -> Optional[bool]: Validates a password
    using a pattern associated with the character sequence.
- main(): Runs the password generator program.

Classes:
- ConstCommands: Contains constant values for user commands.
- ConstColors: Contains constant values for terminal colors.
- ConstPassConfig: Contains constant values for password configuration options.
- ConstPatternStrength: Contains constant values for password strength patterns.

Modules Used:
- re: For regular expressions.
- string: For string constants.
- random: For generating random selections.
- termcolor: For coloring terminal output.
- typing: For type hinting.

"""

import re
import string
import random
from termcolor import cprint, colored


class ConstCommands:
    YES = "y"


class ConstColors:
    COLOR_GREEN = "green"
    COLOR_CYAN = "cyan"
    COLOR_YELLOW = "yellow"
    COLOR_MAGENTA = "magenta"


class ConstPassConfig:
    MIN_LENGTH = 4
    LENGTH = "length"
    MENU_OPTIONS = "options"

    STRING_LOWER = "lower"
    STRING_UPPER = "upper"
    STRING_NUMBERS = "numbers"
    STRING_SYMBOLS = "symbols"

    INCLUDE_UPPER = "include_upper"
    INCLUDE_DIGITS = "include_digits"
    INCLUDE_SYMBOLS = "include_symbols"


class ConstPatternStrength:
    WEAK = "weak"
    MEDIUM = "medium"
    STRONG = "strong"
    VERY_STRONG = "very_strong"
    END = "end"


menu_options = {
    ConstPassConfig.LENGTH: "\nEnter a password length: ",
    ConstPassConfig.MENU_OPTIONS: {
        ConstPassConfig.INCLUDE_UPPER: "Include uppercase letters (y/n): ",
        ConstPassConfig.INCLUDE_DIGITS: "Include numbers? (y/n): ",
        ConstPassConfig.INCLUDE_SYMBOLS: "Include special characters? (y/n): ",
    },
}


char_sequences = {
    ConstPassConfig.STRING_LOWER: string.ascii_lowercase,
    ConstPassConfig.STRING_UPPER: string.ascii_uppercase,
    ConstPassConfig.STRING_NUMBERS: string.digits,
    ConstPassConfig.STRING_SYMBOLS: string.punctuation,
}


patterns = {
    ConstPatternStrength.WEAK: r"^(?=.*[a-z])",
    ConstPatternStrength.MEDIUM: r"(?=.*[A-Z])",
    ConstPatternStrength.STRONG: r"(?=.*\d)",
    ConstPatternStrength.VERY_STRONG: r"(?=.*[!#$%&'()*+\-:<=>?@[\\\]_/])",
    ConstPatternStrength.END: r".+$",
}


def get_pass_length() -> int:
    """Prompts the user to enter the password length"""
    while True:
        try:
            length = int(
                input(
                    colored(
                        menu_options[ConstPassConfig.LENGTH], ConstColors.COLOR_CYAN
                    )
                ).strip()
            )
            if length >= ConstPassConfig.MIN_LENGTH:
                return length

            raise ValueError()
        except ValueError:
            cprint(
                f"\nPassword must be at least 4 characters long",
                ConstColors.COLOR_MAGENTA,
            )


def get_settings() -> dict:
    """Prompts the user to choose password configurations"""
    settings = {
        ConstPassConfig.INCLUDE_UPPER: False,
        ConstPassConfig.INCLUDE_DIGITS: False,
        ConstPassConfig.INCLUDE_SYMBOLS: False,
    }
    for key, option in (menu_options[ConstPassConfig.MENU_OPTIONS]).items():
        user_input = input(colored(option, ConstColors.COLOR_CYAN)).lower().strip()

        if user_input == ConstCommands.YES:
            settings[key] = True
        else:
            settings[key] = False

    return settings


def get_configs(char_sequences: str, settings: dict) -> tuple:
    """Returns one of the 8 possible variants of the character sequence string
    and a pattern for generating a valid password."""
    sequence = char_sequences[ConstPassConfig.STRING_LOWER]
    pattern = [patterns[ConstPatternStrength.WEAK], patterns[ConstPatternStrength.END]]

    if settings[ConstPassConfig.INCLUDE_UPPER]:
        sequence += char_sequences[ConstPassConfig.STRING_UPPER]
        pattern.insert(-1, patterns[ConstPatternStrength.MEDIUM])

    if settings[ConstPassConfig.INCLUDE_DIGITS]:
        sequence += char_sequences[ConstPassConfig.STRING_NUMBERS]
        pattern.insert(-1, patterns[ConstPatternStrength.STRONG])

    if settings[ConstPassConfig.INCLUDE_SYMBOLS]:
        sequence += char_sequences[ConstPassConfig.STRING_SYMBOLS]
        pattern.insert(-1, patterns[ConstPatternStrength.VERY_STRONG])

    return sequence, "".join(pattern)


def generate_password(sequence: str, length: int, pattern: str) -> str:
    """Generates a password based on user's configurations"""

    while True:
        password = "".join(random.sample(sequence, length))
        if validate_password(password, pattern):
            return password
        continue


def validate_password(password: str, pattern: str) -> bool:
    """Validate a password using a pattern associated with chracter sequence"""
    return bool(re.match(pattern, password))


def main():
    """Runs pass generator programm"""
    while True:
        try:
            length = get_pass_length()
            settings = get_settings()
            sequence, pattern = get_configs(char_sequences, settings)
            if length > len(sequence):
                raise ValueError()

            password = generate_password(sequence, length, pattern)

            cprint(
                f"\nYour password is: {colored(password, ConstColors.COLOR_YELLOW)}\n"
            )
            break
        except ValueError:
            cprint(
                f"\nPassword length can be max {len(sequence)} characters long",
                ConstColors.COLOR_MAGENTA,
            )


if __name__ == "__main__":
    main()
