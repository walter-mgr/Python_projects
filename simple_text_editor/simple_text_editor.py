import os
import re
from termcolor import colored, cprint
from enum import Enum


class ConstantsColors:
    COLOR_RED = "red"
    COLOR_GREEN = "green"
    COLOR_CYAN = "cyan"


class ConstantsErrors:
    INVALID_FILENAME_ERROR = "1"


class ConstantsCommands:
    SAVE = "SAVE"


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


# file_path = os.path.join(os.path.dirname(__file__), "test.txt")


def read_from_existing_file(file_path):

    try:
        with open(file_path, "r") as file:
            contents = file.read()
            print(f"\n{contents}")
    except FileNotFoundError:
        print("File does not exist.")


def open_or_update_file(file_path):
    if file_path:
        read_from_existing_file(file_path)

    cprint(
        "\nEnter your text (type SAVE on a new line to save and exit):",
        ConstantsColors.COLOR_GREEN,
    )

    with open(file_path, "w") as file:
        while True:
            try:
                line = input()
                if line.upper() == ConstantsCommands.SAVE:
                    break
                file.write(line + "\n")

            except FileNotFoundError:
                print("File does not exist.")


def main():

    filename = get_valid_filename()

    file_path = os.path.join(os.path.dirname(__file__), filename)

    open_or_update_file(file_path)

    cprint(f"{filename} saved", ConstantsColors.COLOR_CYAN)


if __name__ == "__main__":
    main()
    # read_from_existing_file(file_path)


"""
TASK DESCRIPTION

# 1. Round / cycle

# Enter the filename to open or create: somefile.txt

# Enter your text (type SAVE on a new line to save and exist):
#   Some text
#   Some text
#   Some text

# SAVE

# Recieve a masage: somefile.txt saved

# 2. Round / cycle

# Enter the filename to open or create: somefile.txt

# Read old data:
#       Some text   (old data)
#       Some text   (old data)
#       Some text   (old data)

# Enter your text (type SAVE on a new line to save and exist):

#   New data
#   New data
#   New data

# SAVE

# Recieve a masage: somefile.txt saved

"""
