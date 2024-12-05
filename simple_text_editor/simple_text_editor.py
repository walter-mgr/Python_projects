import os
import re
from termcolor import colored, cprint


class ConstColors:
    """Class to store color constants for terminal output."""

    COLOR_RED = "red"
    COLOR_GREEN = "green"
    COLOR_CYAN = "cyan"
    COLOR_YELLOW = "yellow"


class ConstCommands:
    """Class to store command constants."""

    SAVE = "SAVE"


class ConstFileEditMode:
    """Class to store file edit mode constants and file validation patterns."""

    FILE_WRITE = "w"
    FILE_READ = "r"
    FILE_ALLOWED_EXTENTIONS = {".txt"}
    FILE_CHARS_FORBIDDEN_PATTERN = r"[<>:/\\|?*]"


class ConstErrors:
    """Class to store error code constants."""

    INVALID_FILENAME_ERROR = "1"

    error_messages = {
        INVALID_FILENAME_ERROR: colored(
            "Please enter a valid filename", ConstColors.COLOR_RED
        )
    }


def is_valid_character(filename: str, pattern: str) -> bool:
    """Check if the filename contains any forbidden characters."""
    return not any(re.search(pattern, char) for char in filename)


def is_valid_length(filename: str) -> bool:
    """Check if the filename length is within the allowed limit."""
    return len(filename) <= 50


def is_valid_extention(filename: str, allowed_extention: set) -> bool:
    """Check if the filename has a valid extension."""
    _, ext = os.path.splitext(filename)
    return ext in allowed_extention


def is_valid_filename(filename: str, pattern: str) -> bool:
    """Prompt the user to input a valid filename."""
    return (
        is_valid_character(filename, pattern)
        and is_valid_length(filename)
        and is_valid_extention(filename, ConstFileEditMode.FILE_ALLOWED_EXTENTIONS)
    )


def get_valid_filename() -> str:
    """Prompt the user to input a valid filename."""
    while True:
        filename = (
            input(colored("\nEnter a filename: ", ConstColors.COLOR_YELLOW))
            .lower()
            .strip()
        )
        if (
            is_valid_filename(filename, ConstFileEditMode.FILE_CHARS_FORBIDDEN_PATTERN)
            and filename
        ):
            return filename
        print(ConstErrors.error_messages[ConstErrors.INVALID_FILENAME_ERROR])


def read_from_existing_file(file_path: str, filename: str) -> None:
    """Read and display contents from an existing file."""
    print_filename_cyan = colored(filename, ConstColors.COLOR_CYAN)
    try:

        with open(file_path, ConstFileEditMode.FILE_READ) as file:
            contents = file.read()
            if not contents:
                cprint("\nNo content in this file", ConstColors.COLOR_CYAN)
            print(f"\n{contents}")

    except FileNotFoundError:
        cprint(
            f"\nFile '{print_filename_cyan}' was successfully created.\n",
            ConstColors.COLOR_GREEN,
        )


def create_or_update_file(file_path: str, filename: str) -> None:
    """Create a new file or update an existing file with user input."""
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


def main() -> None:
    """Main function to run the file management program."""
    filename = get_valid_filename()
    file_path = os.path.join(os.path.dirname(__file__), filename)
    create_or_update_file(file_path, filename)


if __name__ == "__main__":
    main()


"""
TASK DESCRIPTION

# 1. Round / cycle

# Enter the filename to open or create: somefile.txt

# Enter your text (type SAVE on a new line to save and exit):
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
