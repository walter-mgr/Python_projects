""" Word-Guessing Game
This project is a word-guessing game where the player attempts to guess a secret
word one letter at a time. The game provides feedback on each guess, indicating
whether the guess is correct or not. The player wins by guessing all the letters in
the secret word within a limited number of attempts.

Project Description:
1. **Reading Words**: The game reads a list of words from a file ('words.txt').
    The words are stored in a list.
2. **Choosing a Random Word**: A random word is selected from the list to be the
    secret word for the game.
3. **Displaying the Secret Word**: The secret word is initially displayed as underscores,
    representing unguessed letters.
4. **Taking User Guesses**: The player inputs a single letter as a guess. The input
    is validated to ensure it's a lowercase letter.
5. **Updating the Display**: If the guessed letter is in the secret word, it is revealed
    in the display. Otherwise, an attempt is counted as wrong.
6. **Tracking Guesses**: The game tracks the letters guessed by the player to prevent
    repeated guesses.
7. **Ending the Game**: The game ends when the player either guesses the word correctly or exhausts the maximum number of wrong attempts.

Functions:
- read_file(file_path: str) -> list: Reads the file and returns a list of words.
- get_random_word(words_list: list) -> str: Returns a random word from the list of words.
- print_secret(secret_word: str, guesses: set) -> None: Prints the secret word with
    guessed letters revealed and others hidden.
- get_user_input(guessed_letters: set) -> str: Gets valid user input and ensures the
    letter hasn't been guessed before.
- guess_word(wrong_attempts: int, secret_word: str, guessed_letters: set) -> None: Manages
    the guessing process and tracks attempts and guesses.
- main(): Runs the word-guessing game.

Classes:
- GameConfig: Stores game configuration constants such as the quit command, filename,
    file read mode, and maximum attempts.

Modules Used:
- os: For handling file paths.
- re: For regular expressions to validate user input.
- random: For selecting a random word from the list.

Example Usage:
Run the script to start the game. The player will be prompted to enter a letter, and
the game will provide feedback on the guess. If the player guesses the word before
running out of attempts, they win. Otherwise, they lose, and the correct word is revealed.
"""

import os
import re
import random


class GameConfig:
    QUIT = "0"
    FILENAME = "words.txt"
    READ = "r"
    MAX_ATTEMPTS = 6
    ALLOWED_LETTERS = r"^[a-z]$"


file_path = os.path.join(os.path.dirname(__file__), GameConfig.FILENAME)


def read_file(file_path: str) -> list:
    """Reads from the file and returns a list of words."""
    try:
        with open(file_path, GameConfig.READ) as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("File does not exist.")
        return []


def get_random_word(words_list: list) -> str:
    """Returns a random word from the list of words."""
    if not words_list:
        print("No words loaded.")
        return ""
    return random.choice(words_list)


def print_secret(secret_word: str, guesses: str) -> None:
    """Prints a word with all characters replaced by underscores."""
    display_word = "".join([char if char in guesses else "_" for char in secret_word])
    print(display_word)


def get_user_input(guessed_letters: set) -> str:
    """Gets valid user input and checks if letter has already been guessed."""
    while True:
        user_input = input("Enter a letter: ").lower().strip()
        if user_input == GameConfig.QUIT:
            return GameConfig.QUIT

        if len(user_input) != 1:
            print("Enter only one letter")

        elif not re.search(GameConfig.ALLOWED_LETTERS, user_input):
            print("Enter only letters from 'a' to 'z'.")

        elif user_input in guessed_letters:
            print("You already guessed that letter.")

        else:
            return user_input


def guess_word(wrong_attempts: int, secret_word: str, guessed_letters: str) -> None:
    """Manages the guessing process for the word-guessing game."""
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


def main():
    """Runs the word guessing game."""
    # words_list = read_file(file_path)
    # secret_word = get_random_word(words_list)
    # if not secret_word:
    # return
    guessed_letters = set()
    # wrong_attempts = 0
    # guess_word(wrong_attempts, secret_word, guessed_letters)
    get_user_input(guessed_letters)


if __name__ == "__main__":
    main()
