# In the file 'words.txt' we have a bunch of words
# Read from the file a list of words / Done
# Choose a random word / Done
# Convert a random word to output like this:  _____ and print (word) / Done
# Take user guess / Done
# Example word: horse
# Example output: _____
# If user guess is right: show a letter: _o___
# Otherwise: Ask user for another try

# Good guess
# a_____a__

# Enter a letter: a
#   Error message: You already guessed that letter.

# Enter a letter: x
# Wrong guess
# a_____a__
#
# Enter a letter: x
#
# Maximmum of wrong attempts is 6

import os
import re
import random
import string


class GameConfig:
    QUIT = "0"
    FILENAME = "words.txt"
    READ = "r"
    MAX_ATTEMPTS = 6


file_path = os.path.join(os.path.dirname(__file__), GameConfig.FILENAME)


def read_file(file_path: str) -> list:
    """This function reads from the file and returns a list of words."""
    with open(file_path, GameConfig.READ) as file:
        return file.read().splitlines()


def get_random_word(words_list: list) -> str:
    """This function returns a random word from the list of words."""
    return random.choice(words_list)


def print_secret(secret_word: str, guesses: str):
    """Prints a word with all characters replaced by underscores."""
    display_word = "".join([char if char in guesses else "_" for char in secret_word])
    print(display_word)


def get_user_input(guessed_letters: set) -> str:
    """Gets valid user input and checks if letter has already been guessed."""
    is_valid = r"^[a-z]$"

    while True:
        user_input = input("Enter a letter: ").lower().strip()
        if user_input == GameConfig.QUIT:
            return GameConfig.QUIT

        if user_input in guessed_letters:
            print("You alredy guessed that letter.")
            continue

        if user_input and re.match(is_valid, user_input):
            return user_input

        if len(user_input) > 1:
            print("Enter only one letter")
            continue
        print("Enter only letters from a to z.")
        continue


def main():
    words_list = read_file(file_path)
    secret_word = get_random_word(words_list)
    guessed_letters = set()
    wrong_attempts = 0
    print(secret_word)  # Remove me when done

    while wrong_attempts < GameConfig.MAX_ATTEMPTS:

        print_secret(secret_word, guessed_letters)
        guess = get_user_input(guessed_letters)

        if guess == GameConfig.QUIT:
            break

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess!")
            if all(char in guessed_letters for char in secret_word):
                print(f"Congradulations! You've guessed a word: {secret_word}")
                break
        else:
            wrong_attempts += 1
            print(
                f"Wrong guess. Attempts left: {GameConfig.MAX_ATTEMPTS - wrong_attempts}"
            )

        if wrong_attempts == GameConfig.MAX_ATTEMPTS:
            print(f"Game over. Word to guess was: {secret_word}")


if __name__ == "__main__":
    main()
