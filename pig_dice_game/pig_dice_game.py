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
    COLOR_YELLOW = "yellow"
    COLOR_MAGENTA = "light_magenta"


def roll_dice() -> int:
    return randint(1, 6)


def switch_player(current_player: str) -> str:
    return PLAYER_TWO if current_player == PLAYER_ONE else PLAYER_ONE


def print_current_score(current_score: int) -> None:
    cprint(f"\nYou scored {current_score} this turn", ConstColors.COLOR_MAGENTA)


def print_total_scores(total_score_one, total_score_two) -> None:
    cprint(
        f"Current scores: Player 1: {total_score_one}, Player 2: {total_score_two}\n",
        ConstColors.COLOR_MAGENTA,
    )


def play_turn(current_player, total_score_one, total_score_two):
    current_score = 0
    while True:
        dice = roll_dice()
        if dice == 1:
            cprint(f"You rolled a {dice}", ConstColors.COLOR_RED)
            current_score = 0
            print_current_score(current_score)
            break
        else:
            current_score += dice
            cprint(f"You rolled a {dice}", ConstColors.COLOR_CYAN)

        player_choice = input("Roll again? (y/n): ").lower().strip()
        if player_choice == EXIT:
            return current_player, total_score_one, total_score_two, True

        if player_choice == NO:
            print_current_score(current_score)
            break

    if current_player == PLAYER_ONE:
        total_score_one += current_score
    else:
        total_score_two += current_score

    return current_player, total_score_one, total_score_two, False


def main():
    total_score_one = 0
    total_score_two = 0
    current_player = PLAYER_ONE
    game_over = False
    cprint("PIG DICE GAME", ConstColors.COLOR_CYAN, attrs=["reverse"])

    while not game_over:
        cprint(f"\nPlayer {current_player}'s turn", ConstColors.COLOR_YELLOW)
        current_player, total_score_one, total_score_two, game_over = play_turn(
            current_player, total_score_one, total_score_two
        )
        print_total_scores(total_score_one, total_score_two)
        if total_score_one >= GAME_LIMIT or total_score_two >= GAME_LIMIT:
            cprint(f"Player {current_player} is winner!", ConstColors.COLOR_GREEN)
            game_over = True
        else:
            current_player = switch_player(current_player)


if __name__ == "__main__":
    main()


"""
# TASK DESCRIPTION

# While Loop

# Print a message whose player turn is
    # Call random function
    # Take user input if continue or not
    # Store rolled points for each player
        
        
        
        
        


    # Player 1's turn
    #   You rolled a 6
    #   Roll again? (y/n): y
    #   You rolled a 3
    #   Roll again? (y/n): y
    #   You rolled a 5
    #   Roll again? (y/n): y

    # Points are collecting 6 + 3 + 5
    
    #   If roll == 1:
            Current players score == 0
                Need to do: reset only scores from this round
                All scores from the previous rounds must stay saved
            Automatically switch a player

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


"""
