from random import randint
from termcolor import colored, cprint

PLAYER_ONE = "1"
PLAYER_TWO = "2"
NO = "n"
EXIT = "q"
GAME_LIMIT = 50


class ConstColors:
    COLOR_GREEN = "green"
    COLOR_CYAN = "cyan"
    COLOR_RED = "red"


def main():
    total_score_one = 0
    total_score_two = 0

    current_player = PLAYER_ONE
    current_score = total_score_one

    print(f"Player {current_player}'s turn")

    while True:

        dice = randint(1, 6)

        if dice == 1:

            if current_player == PLAYER_ONE:
                current_score = 0
                total_score_one = current_score
            else:
                current_score = 0
                total_score_two = current_score

            cprint(f"You rolled a {dice}", ConstColors.COLOR_RED)
            print(f"\nYou scored {current_score} points this turn.")
            print(
                f"Current scores: Player 1: {total_score_one}, Player 2: {total_score_two}\n"
            )
            current_player = PLAYER_TWO if current_player == PLAYER_ONE else PLAYER_ONE
            print(f"Player {current_player}'s turn")
            continue

        if current_player == PLAYER_ONE:
            total_score_one += dice
            current_score = total_score_one
        else:
            total_score_two += dice
            current_score = total_score_two
        print(f"You rolled a {dice}")

        player_choice = input("Roll again? (y/n): ").lower().strip()
        if player_choice == EXIT:
            break

        if player_choice == NO:
            print(f"\nYou scored {current_score} points this turn.")
            if current_player == PLAYER_ONE:
                total_score_one = current_score
            else:
                total_score_two = current_score
            print(
                f"Current scores: Player 1: {total_score_one}, Player 2: {total_score_two}\n"
            )
            if total_score_one >= 50 or total_score_two >= 50:
                cprint(f"Player {current_player} is winner!")
                break
            current_player = PLAYER_TWO if current_player == PLAYER_ONE else PLAYER_ONE
            print(f"Player {current_player}'s turn")


main()


"""
# TASK DESCRIPTION

# While Loop

# Print a message whose player turn is
    # Call random function
    # Take user input if continue or not
    # Store rolled points for each player
        # If roll == 1:
            Current players score == 0
            Automatically switch a player


    # Player 1's turn
    #   You rolled a 6
    #   Roll again? (y/n): y
    #   You rolled a 3
    #   Roll again? (y/n): y
    #   You rolled a 5
    #   Roll again? (y/n): y

    # Points are collecting 6 + 3 + 5
    #   If roll a 1 all points are gone
    #       Turn ends

    # Messages:
    #   You scored 14 points this turn.
    #   Current scores: Player 1: 14, Player 2: 0

    # Player 2's turn
    #   You rolled a 6
    #   Roll again? (y/n): y
    #   You rolled a 1

    # Messages:
    #   You scored 0 points this turn.
    #   Current scores: Player 1: 14, Player 2: 0

    # The game repeats until one of the player reaches 100 points
"""

"""
1. This version resets total player's score 

if dice == 1:
    if current_player == PLAYER_ONE:
        total_score_one = 0
        current_score = total_score_one

    else:
        total_score_two = 0
        current_score = total_score_two

2. This version resets only current player's score

if dice == 1:
    if current_player == PLAYER_ONE:
        current_score = 0
    else:
        current_score = 0

"""
