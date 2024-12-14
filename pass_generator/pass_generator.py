"""Password Generator Programm"""

import re
import string
import random


# Define a data structure for this project / done
class ConstCommands:
    QUIT = "q"
    YES = "y"


class ConstPassConfig:
    LENGTH = "1"
    INCLUDE_NUMBERS = "2"
    INCLUDE_UPPER = "3"
    INCLUDE_SPEC_CHAR = "4"
    MIN_LENGTH = "4"


"""
config_options = {
    ConstPassConfig.LENGTH: "Enter a password length: ",
    ConstPassConfig.INCLUDE_UPPER: "Include uppercase letters (y/n): ",
    ConstPassConfig.INCLUDE_NUMBERS: "Include numbers? (y/n): ",
    ConstPassConfig.INCLUDE_SPEC_CHAR: "Include special characters? (y/n): ",
}
"""
config_options = [
    "Enter a password length: ",
    "Include uppercase letters (y/n): ",
    "Include numbers? (y/n): ",
    "Include special characters? (y/n): ",
]


pass_data = {
    "letters_lower": string.ascii_lowercase,
    "digits": string.digits,
    "letters_upper": string.ascii_uppercase,
    "symbols": "!@#$%^&*()|/\\",
}


length = 4
pattern = rf"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*]).{{{length}}}$"

sequence = (
    pass_data["letters_lower"]
    # + pass_data["digits"]
    # + pass_data["symbols"]
    # + pass_data["letters_upper"]
)


def generate_valid_password(sequence, pattern, length):
    while True:
        password = "".join(random.sample(sequence, length))
        if re.match(pattern, password):
            return password
