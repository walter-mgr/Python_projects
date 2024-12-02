import os
import re
from termcolor import colored
from enum import Enum


class ConstantsColors:
    COLOR_RED = "red"


class ConstantsErrors:
    INVALID_FILENAME_ERROR = "1"


file_path = os.path.join(os.path.dirname(__file__), "test.txt")

error_messages = {
    "1": colored("Please enter a valid filename", ConstantsColors.COLOR_RED)
}

forbidden_chars_pattern = r"[<>:/\\|?*]"


def is_valid_charachter(filename, forbidden_chars_pattern):
    for char in filename:
        if re.search(forbidden_chars_pattern, char):
            return False
    return True


def is_valid_length(filename):
    if len(filename) > 50:
        return False
    return True


def is_valid_filename(filename, forbidden_chars_pattern):
    if is_valid_charachter(filename, forbidden_chars_pattern) and is_valid_length(
        filename
    ):
        return True


def get_valid_filename():
    while True:
        try:
            filename = input("Enter a filename: ").lower().strip()
            if is_valid_filename(filename, forbidden_chars_pattern) and filename:
                return filename
            raise ValueError()
        except ValueError:
            print(error_messages[ConstantsErrors.INVALID_FILENAME_ERROR])


def append_line_to_file(path, message):
    try:
        with open(path, "a") as file:
            file.write(f"{message}")
    except FileNotFoundError:
        print("The file does not exist.")


# 1. Round / cycle
# Enter the filename to open or create: somefile.txt

get_valid_filename()
# get_file_name()

# Enter your text (type SAVE on a new line to save and exist):
#   Some text
#   Some text
#   Some text

# SAVE

# Recieve a masage: somefile.txt saved

# 2. Round / cycle

# Enter the filename to open or create: somefile.txt
#   Some text   (old data)
#   Some text   (old data)
#   Some text   (old data)

# Enter your text (type SAVE on a new line to save and exist):

#   New data
#   New data
#   New data

# SAVE

# Recieve a masage: somefile.txt saved


message = "\nHi! I've just created a new file"
# message = input()


def create_or_update_file(path, message):
    try:
        with open(path, "w") as file:
            file.write(f"{message}")
    except FileNotFoundError:
        print("The file doesn't exist.")


# create_or_update_file(file_path, message)
# append_line_to_file(file_path, message)
