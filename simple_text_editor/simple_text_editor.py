import os
import re
from termcolor import colored, cprint


class ConstColors:
    COLOR_RED = "red"
    COLOR_GREEN = "green"
    COLOR_CYAN = "cyan"
    COLOR_YELLOW = "yellow"


class ConstErrors:
    INVALID_FILENAME_ERROR = "1"


class ConstCommands:
    SAVE = "SAVE"


class ConstFileEditMode:
    FILE_WRITE = "w"
    FILE_READ = "r"


error_messages = {"1": colored("Please enter a valid filename", ConstColors.COLOR_RED)}

forbidden_chars_pattern = r"[<>:/\\|?*]"


def is_valid_character(filename, forbidden_chars_pattern):
    for char in filename:
        if re.search(forbidden_chars_pattern, char):
            return False
    return True


def is_valid_length(filename):
    return len(filename) <= 50


def is_valid_filename(filename, forbidden_chars_pattern):
    return is_valid_character(filename, forbidden_chars_pattern) and is_valid_length(
        filename
    )


def get_valid_filename():
    while True:
        filename = (
            input(colored("\nEnter a filename: ", ConstColors.COLOR_YELLOW))
            .lower()
            .strip()
        )
        if is_valid_filename(filename, forbidden_chars_pattern) and filename:
            return filename
        print(error_messages[ConstErrors.INVALID_FILENAME_ERROR])


def read_from_existing_file(file_path, filename):
    print_cyan = colored(filename, ConstColors.COLOR_CYAN)
    try:

        with open(file_path, ConstFileEditMode.FILE_READ) as file:
            contents = file.read()
            if not contents:
                cprint("\nNo content in this file", ConstColors.COLOR_YELLOW)
            print(f"\n{contents}")

    except FileNotFoundError:
        cprint(
            f"\nFile '{print_cyan}' was successfully created.\n",
            ConstColors.COLOR_GREEN,
        )


def open_and_update_file(file_path, filename):
    if file_path:
        read_from_existing_file(file_path, filename)
    cprint(
        "Enter your text (type SAVE on a new line to save and exit):",
        ConstColors.COLOR_GREEN,
    )

    with open(file_path, ConstFileEditMode.FILE_WRITE) as file:
        while True:

            line = input()
            if line.upper() == ConstCommands.SAVE:
                break
            file.write(line + "\n")
        cprint(f"{filename} saved", ConstColors.COLOR_CYAN)

    # print("File does not exist.")


def main():
    filename = get_valid_filename()
    file_path = os.path.join(os.path.dirname(__file__), filename)
    open_and_update_file(file_path, filename)


if __name__ == "__main__":
    main()
    # print(get_valid_filename())


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
