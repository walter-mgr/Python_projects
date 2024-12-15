"""Password Generator Programm"""

import re
import string
import random


class ConstCommands:

    YES = "y"


class ConstPassConfig:
    MIN_LENGTH = 4
    LENGTH = "length"
    CONFIG_OPTIONS = "options"
    STRING_LOWER = "lower"
    STRING_UPPER = "upper"
    STRING_NUMBERS = "numbers"
    STRING_SYMBOLS = "symbols"


class ConstPatternStrong:
    WEAK = "weak"
    MEDIUM = "medium"
    STRONG = "strong"
    VERY_STRONG = "very_strong"


config_options = {
    ConstPassConfig.LENGTH: "Enter a password length: ",
    ConstPassConfig.CONFIG_OPTIONS: [
        "Include uppercase letters (y/n): ",
        "Include numbers? (y/n): ",
        "Include special characters? (y/n): ",
    ],
}


pass_data = {
    "letters_lower": string.ascii_lowercase,
    "digits": string.digits,
    "letters_upper": string.ascii_uppercase,
    "symbols": "!@#$%^&*()|/",
}

# sequence = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+-:<=>?@[]_/"
char_sequence = {
    "lower": string.ascii_lowercase,
    "upper": string.ascii_uppercase,
    "digits": string.digits,
    "symbols": "!#$%&'()*+-:<=>?@[]_/",
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
            print("Password must be at least 4 characters long")


patterns = {
    ConstPatternStrong.WEAK: r"^[a-z]+$",
    ConstPatternStrong.MEDIUM: r"^[A-Za-z]+$",
    ConstPatternStrong.STRONG: r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])[A-Za-z\d]+$",
    ConstPatternStrong.VERY_STRONG: r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!#$%&'()*+-:<=>?@[]_/]).+$",
}


def get_pass_config() -> dict:
    pass_config = []
    for option in config_options[ConstPassConfig.CONFIG_OPTIONS]:
        user_input = input(option).lower().strip()

        if user_input == ConstCommands.YES:
            pass_config.append(True)
        else:
            pass_config.append(False)

    return {"1": pass_config[0], "2": pass_config[1], "3": pass_config[2]}


pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?:{}|<>]).{4,}$"


def generate_password(sequence, length):
    password = "".join(random.choices(sequence, k=length))
    return password


def validate_password():
    pass


def get_sequence(char_sequence, settings):
    """Returns one of the 8 possible variants of the character sequence string"""
    sequence = char_sequence["lower"]
    # true false false
    if settings["1"] and not settings["2"] and not settings["3"]:
        return sequence + char_sequence["upper"]
    # false true false
    if not settings["1"] and settings["2"] and not settings["3"]:
        return sequence + char_sequence["digits"]
    # false false true
    if not settings["1"] and not settings["2"] and settings["3"]:
        return sequence + char_sequence["symbols"]
    # true true false
    if settings["1"] and settings["2"] and not settings["3"]:
        return sequence + char_sequence["upper"] + char_sequence["digits"]
    # false true true
    if not settings["1"] and settings["2"] and settings["3"]:
        return sequence + char_sequence["digits"] + char_sequence["symbols"]
    # true false true
    if settings["1"] and not settings["2"] and settings["3"]:
        return sequence + char_sequence["upper"] + char_sequence["symbols"]
    # true true true
    if settings["1"] and settings["2"] and settings["3"]:
        return (
            char_sequence["lower"]
            + char_sequence["upper"]
            + char_sequence["digits"]
            + char_sequence["symbols"]
        )

    return sequence


def main():

    length = get_pass_length()
    settings = get_pass_config()
    print(settings)
    # pattern = get_pattern(settings, patterns)
    # print(pattern)
    sequence = get_sequence(char_sequence, settings)
    print(sequence)
    password = generate_password(sequence, length)
    print(password)


if __name__ == "__main__":
    main()
