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
#   Some text   (old data)
#   Some text   (old data)
#   Some text   (old data)

# Enter your text (type SAVE on a new line to save and exist):

#   New data
#   New data
#   New data

# SAVE

# Recieve a masage: somefile.txt saved

from pathlib import Path

file_path = Path("C:/Users/valer/Python_projects/simple_text_editor/test.txt")


"C:/Users/valer/Python_projects/test.py"

message = "Hi! I've just created a new file"


def create_or_update_file(path, message):
    try:
        with open(path, "w") as file:
            contents = file.write(f"{message}")
            print(contents)
    except FileExistsError:
        print("The file doesn't exist.")


def append_line_to_file(path):
    try:
        with open(path, "a") as file:
            contents = file.write("\n'This is a message I write to the file'")
            print(contents)

    except FileNotFoundError:
        print("The file does not exist.")


# append_line_to_file(path)
create_or_update_file(file_path, message)
