"""Password Generator Programm"""

import string
import random
from termcolor import cprint


class ConstCommands:
    YES = "y"


class ConstColors:
    COLOR_RED = "red"


class ConstPassConfig:
    MIN_LENGTH = 4
    LENGTH = "length"
    CONFIG_OPTIONS = "options"

    STRING_LOWER = "lower"
    STRING_UPPER = "upper"
    STRING_NUMBERS = "numbers"
    STRING_SYMBOLS = "symbols"

    INCLUDE_UPPER = "include_upper"
    INCLUDE_DIGITS = "include_digits"
    INCLUDE_SYMBOLS = "include_symbols"


config_options = {
    ConstPassConfig.LENGTH: "Enter a password length: ",
    ConstPassConfig.CONFIG_OPTIONS: [
        "Include uppercase letters (y/n): ",
        "Include numbers? (y/n): ",
        "Include special characters? (y/n): ",
    ],
}


char_sequence = {
    ConstPassConfig.STRING_LOWER: string.ascii_lowercase,
    ConstPassConfig.STRING_UPPER: string.ascii_uppercase,
    ConstPassConfig.STRING_NUMBERS: string.digits,
    ConstPassConfig.STRING_SYMBOLS: "!#$%&'()*+-:<=>?@[]_/",
}


def get_pass_length() -> int:
    """Prompts the user to enter the password length"""
    while True:
        try:
            length = int(input(config_options[ConstPassConfig.LENGTH]).strip())
            if length >= ConstPassConfig.MIN_LENGTH:
                return length
            raise ValueError()
        except ValueError:
            cprint(
                "\nPassword must be at least 4 characters long\n", ConstColors.COLOR_RED
            )


def get_pass_config() -> dict:
    """Prompts the user to choose password configurations"""
    pass_config = []
    for option in config_options[ConstPassConfig.CONFIG_OPTIONS]:
        user_input = input(option).lower().strip()

        if user_input == ConstCommands.YES:
            pass_config.append(True)
        else:
            pass_config.append(False)

    return {
        ConstPassConfig.INCLUDE_UPPER: pass_config[0],
        ConstPassConfig.INCLUDE_DIGITS: pass_config[1],
        ConstPassConfig.INCLUDE_SYMBOLS: pass_config[2],
    }


def generate_password(sequence: str, length: int) -> str:
    """Generates a password based on user's configurations"""
    password = "".join(random.choices(sequence, k=length))
    return password


def get_sequence(char_sequence: str, settings: dict) -> str:
    """Returns one of the 8 possible variants of the character sequence string"""
    sequence = char_sequence[ConstPassConfig.STRING_LOWER]

    if settings[ConstPassConfig.INCLUDE_UPPER]:
        sequence += char_sequence[ConstPassConfig.STRING_UPPER]

    if settings[ConstPassConfig.INCLUDE_DIGITS]:
        sequence += char_sequence[ConstPassConfig.STRING_NUMBERS]

    if settings[ConstPassConfig.INCLUDE_SYMBOLS]:
        sequence += char_sequence[ConstPassConfig.STRING_SYMBOLS]

    return sequence


def main():
    """Runs pass generator programm"""

    length = get_pass_length()
    settings = get_pass_config()
    sequence = get_sequence(char_sequence, settings)
    password = generate_password(sequence, length)
    print(password)


if __name__ == "__main__":
    main()
