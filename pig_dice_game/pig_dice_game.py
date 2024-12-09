"""
TASK DESCRIPTION:
This module implements a two-player dice game where players take turns rolling a dice.
The game continues until one player reaches or exceeds the game limit of 50 points.
Players can choose to roll again or hold their current score. If a player rolls a 1,
their score for that turn is reset to zero, and the turn switches to the other player.
Players can also choose to exit the game at any point.

Functions:
- roll_dice: Simulates rolling a dice.
- switch_player: Switches the active player.
- print_current_score: Prints the current score for the turn.
- print_total_scores: Prints the total scores of both players.
- play_turn: Handles the logic for a single turn of a player.
- determine_winner: Checks if either player has reached the game limit.
- main: Runs the main game loop.
"""

from random import randint
from termcolor import cprint


class ConstPlayers:
    PLAYER_ONE = "1"
    PLAYER_TWO = "2"


class ConstGameOptions:
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
    """Simulate a rolling dice."""
    return randint(1, 6)


def switch_player(current_player: str) -> str:
    """Switch the active player."""
    return (
        ConstPlayers.PLAYER_TWO
        if current_player == ConstPlayers.PLAYER_ONE
        else ConstPlayers.PLAYER_ONE
    )


def print_current_score(current_score: int) -> None:
    """Print the current score for the turn."""
    cprint(f"\nYou scored {current_score} this turn", ConstColors.COLOR_MAGENTA)


def print_total_scores(total_score_one: int, total_score_two: int) -> None:
    """Prints the total scores of both players."""
    cprint(
        f"Current scores: Player 1: {total_score_one}, Player 2: {total_score_two}\n",
        ConstColors.COLOR_MAGENTA,
    )


def play_turn(total_score_one: int, total_score_two: int, current_player: str) -> tuple:
    """Play a single turn for current player."""
    current_score = 0
    while True:
        dice = roll_dice()
        if dice == 1:
            current_score = 0
            cprint(f"You rolled a {dice}", ConstColors.COLOR_RED)
            print_current_score(current_score)
            break
        current_score += dice
        cprint(f"You rolled a {dice}", ConstColors.COLOR_CYAN)

        player_choice = input("Roll again? (y/n): ").lower().strip()
        if player_choice == ConstGameOptions.NO:
            print_current_score(current_score)
            break

        if player_choice == ConstGameOptions.EXIT:
            return total_score_one, total_score_two, current_player, True

    if current_player == ConstPlayers.PLAYER_ONE:
        total_score_one += current_score
    else:
        total_score_two += current_score

    return total_score_one, total_score_two, current_player, False


def determine_winner(
    total_score_one: int, total_score_two: int, game_limit: int
) -> bool:
    """Determine if either player has reached or exceeded the game limit."""
    return total_score_one >= game_limit or total_score_two >= game_limit


def main():
    """Main function to run the game."""
    total_score_one = 0
    total_score_two = 0
    current_player = ConstPlayers.PLAYER_ONE
    cprint("PIG DICE GAME", ConstColors.COLOR_CYAN, attrs=["reverse"])

    while True:
        cprint(f"\nPlayer {current_player}'s turn", ConstColors.COLOR_YELLOW)

        total_score_one, total_score_two, current_player, exit_game = play_turn(
            total_score_one, total_score_two, current_player
        )

        print_total_scores(total_score_one, total_score_two)

        if (
            determine_winner(
                total_score_one, total_score_two, ConstGameOptions.GAME_LIMIT
            )
            or exit_game
        ):
            cprint(f"Player {current_player} is winner!", ConstColors.COLOR_GREEN)
            break

        current_player = switch_player(current_player)


if __name__ == "__main__":
    main()
