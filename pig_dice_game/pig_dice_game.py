from random import randint
from termcolor import colored, cprint

PLAYER_ONE = "1"
PLAYER_TWO = "2"
NO = "n"
EXIT = "q"


class ConstColors:
    COLOR_GREEN = "green"
    COLOR_CYAN = "cyan"
    COLOR_RED = "red"


class ConstPlayersScore:
    PLAYER_ONE_SCORE = colored(0, ConstColors.COLOR_CYAN)
    PLAYER_TWO_SCORE = colored(0, ConstColors.COLOR_GREEN)


"""
def switch_player():
    current_player = None
    current_player = PLAYER_TWO if current_player == PLAYER_ONE else PLAYER_ONE
    return current_player
"""


def add_scores(player, score_one, score_two, dice):
    if player == PLAYER_ONE:
        score_one += dice
        # current_score
        return score_one
    else:
        score_two += dice
        return score_two


def main():
    score_one = 0
    score_two = 0

    current_player = PLAYER_ONE
    current_score = score_one

    print(f"Player {current_player}'s turn")

    while True:
        dice = randint(1, 6)

        if current_player == PLAYER_ONE:
            score_one += dice
            current_score = score_one
        else:
            score_two += dice
            current_score = score_two

        if dice == 1:
            if current_player == PLAYER_ONE:
                # score_one = 0
                # current_score = score_one
                current_score = 0
            else:
                # score_two = 0
                # current_score = score_two
                current_score = 0

            cprint(f"\nYou rolled a {dice}", ConstColors.COLOR_RED)
            print(f"\nYou scored {current_score} points this turn.")
            print(f"Current scores: Player 1: {score_one}, Player 2: {score_two}\n")
            current_player = PLAYER_TWO if current_player == PLAYER_ONE else PLAYER_ONE
            print(f"Player {current_player}'s turn")
            continue

        print(f"You rolled a {dice}")

        player_choice = input("Roll again? (y/n): ").lower().strip()
        if player_choice == EXIT:
            break

        if player_choice == NO:
            print(f"\nYou scored {current_score} points this turn.")
            if current_player == PLAYER_ONE:
                score_one = current_score
            else:
                score_two = current_score
            print(f"Current scores: Player 1: {score_one}, Player 2: {score_two}\n")
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
