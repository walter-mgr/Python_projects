""" Word-Guessing Game
This project is a word-guessing game where the player attempts to guess a secret
word one letter at a time. The game provides feedback on each guess, indicating
whether the guess is correct or not. The player wins by guessing all the letters in
the secret word within a limited number of attempts.

Project Description:
1. **Reading Words**: The game reads a list of words from a file ('words.json').
    The words are stored as key-value pairs in a dictionary within a list.
2. **Choosing a Random Word**: A random dictionary is selected from the list to provide
    the secret word and its hint for the game.
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
- read_file(file_path: str) -> list: Reads the file and returns a list of dictionaries.
- get_random_dict(words_list: list) -> dict: Returns a random dictionary from the list
    of dictionaries.
- get_word_and_hint(word_to_guess: dict) -> Tuple[str, str]: Returns the first
    key-value pair from the dictionary.
- display_secret_word(secret_word: str, guesses: set) -> None: Prints the secret word
    with guessed letters revealed and others hidden.
- get_user_input(guessed_letters: set) -> str: Gets valid user input and ensures the
    letter hasn't been guessed before.
- guess_word(wrong_attempts: int, secret_word: str, hint: str, guessed_letters: set) ->
    None: Manages the guessing process and tracks attempts and guesses.
- main(): Runs the word-guessing game.

Classes:
- GameConfig: Stores game configuration constants such as the quit command, filename,
    file read mode, and maximum attempts.
- Colors: Stores color constants for printing colored text.

Modules Used:
- os: For handling file paths.
- re: For regular expressions to validate user input.
- random: For selecting a random word from the list.
- json: For reading and decoding JSON files.
- termcolor: For printing colored text to the terminal.

Example Usage:
Run the script to start the game. The player will be prompted to enter a letter, and
the game will provide feedback on the guess. If the player guesses the word before
running out of attempts, they win. Otherwise, they lose, and the correct word is revealed.
"""

import os
import re
import random
import json
from termcolor import cprint, colored
from typing import Tuple


class Colors:
    GREEN = "green"
    BLUE = "cyan"
    YELLOW = "yellow"
    RED = "red"


class GameConfig:
    QUIT = "0"
    FILENAME = "words.json"
    READ = "r"
    MAX_ATTEMPTS = 6
    ALLOWED_LETTERS = r"^[a-z]$"


file_path = os.path.join(os.path.dirname(__file__), GameConfig.FILENAME)


def read_file(file_path: str):
    """Reads from the file and returns a list of dictionaries."""
    try:
        with open(file_path, GameConfig.READ) as file:
            data = json.load(file)
            return [{key: value} for key, value in data.items()]
    except FileNotFoundError:
        cprint("File does not exist.", Colors.RED)
        return []
    except json.JSONDecodeError:
        cprint("Failed to decode JSON.", Colors.RED)
        return []


def get_random_dict(words_list: list) -> dict:
    """Returns a random dictionary from the list of dictionaries."""
    if not words_list:
        cprint("No data loaded.", Colors.RED)
        return {}
    word_dict = random.choice(words_list)
    return word_dict


def get_word_and_hint(word_to_guess: dict) -> Tuple[str, str]:
    """Returnes a tuple of secret word and a hint to guess the secret word."""
    if not word_to_guess:
        cprint("The dictionary is empty.", Colors.RED)
        return tuple()
    for key, value in word_to_guess.items():
        return key, value


def display_secret_word(secret_word: str, guesses: str) -> None:
    """Prints a word with all characters replaced by underscores."""
    cprint(
        "".join([char if char in guesses else "_" for char in secret_word]),
        Colors.YELLOW,
    )


def get_user_input(guessed_letters: set) -> str:
    """Gets valid user input and checks if letter has already been guessed."""
    while True:
        user_input = input(colored("Enter a letter: ", Colors.BLUE)).lower().strip()
        if user_input == GameConfig.QUIT:
            return GameConfig.QUIT

        elif len(user_input) != 1:
            cprint("Enter only one letter", Colors.RED)

        elif not re.search(GameConfig.ALLOWED_LETTERS, user_input):
            cprint("Enter only letters from 'a' to 'z'.", Colors.RED)

        elif user_input in guessed_letters:
            cprint("You already guessed that letter.", Colors.YELLOW)

        else:
            return user_input


def guess_word(
    wrong_attempts: int, secret_word: str, hint: str, guessed_letters: str
) -> None:
    """Manages the guessing process for the word-guessing game."""
    while wrong_attempts < GameConfig.MAX_ATTEMPTS:

        display_secret_word(secret_word, guessed_letters)
        guess = get_user_input(guessed_letters)

        if guess == GameConfig.QUIT:
            break

        guessed_letters.add(guess)

        if guess in secret_word:
            cprint("Good guess!", Colors.GREEN)
            if all(char in guessed_letters for char in secret_word):
                cprint(
                    f"Congradulations! You've guessed a word: {secret_word}",
                    Colors.GREEN,
                )
                break
        else:
            wrong_attempts += 1
            cprint(
                f"Wrong guess. Attempts left: {GameConfig.MAX_ATTEMPTS - wrong_attempts}",
                Colors.RED,
            )

        if wrong_attempts == GameConfig.MAX_ATTEMPTS:
            cprint(f"Game over. Word to guess was: {secret_word}", Colors.GREEN)


def main():
    """Runs the word guessing game."""
    guessed_letters = set()
    wrong_attempts = 0
    cprint("GUESS A WORD\n", Colors.BLUE)
    try:
        words = read_file(file_path)
        secret_dict = get_random_dict(words)
        secret_word, hint = get_word_and_hint(secret_dict)
        print(hint)
        guess_word(wrong_attempts, secret_word, hint, guessed_letters)
    except ValueError:
        cprint("No data in dictionary.", Colors.RED)


if __name__ == "__main__":
    main()
