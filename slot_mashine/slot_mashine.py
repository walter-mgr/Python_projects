""" Slot Machine Game

This is a simple text-based slot machine game where the user can place bets and spin
the reels. The goal is to match three symbols to win a prize. The user starts with a
balance and can continue playing until they run out of money or choose to quit.

Modules:
- random
- termcolor

Classes:
- GameConfig: Configuration for the game.
- Color: Color definitions for text output.

Functions:
- display_balance(balance): Displays current user's balance.
- get_reels(reels): Returns a tuple with three random choices from reel choices.
- get_balance(): Prompts user to enter a valid starting balance.
- get_bet_amount(balance): Prompts user to enter a valid bet amount.
- play_game(balance): Main game loop that handles game play.
- main(): Entry point for the game.
"""

import random
from termcolor import cprint, colored


class GameConfig:
    QUIT = "q"
    REELS = ("🍌", "🍑", "🍒", "🍋", "🥝")


class Color:
    CYAN = "cyan"
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"


def display_balance(balance: int) -> None:
    """Displays current user's balance."""
    cprint(f"\nCurrent balance: 💲{balance:.0f}", Color.YELLOW)


def get_reels(reels: tuple) -> tuple:
    """Returns a tuple with three random choices from reels choices."""
    first = random.choice(reels)
    second = random.choice(reels)
    third = random.choice(reels)
    return first, second, third


def get_balance() -> int:
    """Prompts user to enter a valid starting balance."""
    while True:
        try:
            balance = int(input(colored("Enter your starting balance: 💲", Color.CYAN)))
            if balance <= 0:
                cprint("Balance must be a positive number.", Color.RED)
            else:
                return balance
        except ValueError:
            cprint("Please enter a valid number.", Color.RED)


def get_bet_amount(balance: int) -> int:
    """Prompts user to enter a valid bet amount."""
    while True:
        try:
            bet_amount = int(input(colored("Enter your bet amount: 💲", Color.CYAN)))
            if bet_amount < 1 or bet_amount > balance:
                cprint(
                    f"Invalid bet amount. You can bet between 💲1 and 💲{balance}",
                    Color.RED,
                )
            else:
                return bet_amount
        except ValueError:
            cprint("Please enter a valid number for the bet amount.", Color.RED)


def play_game(balance: int) -> None:
    """Main game loop that handles game play."""
    while balance > 0:
        display_balance(balance)
        bet_amount = get_bet_amount(balance)
        first_reel, second_reel, third_reel = get_reels(GameConfig.REELS)
        print(first_reel, second_reel, third_reel)

        if first_reel == second_reel == third_reel:
            bet_amount *= 10
            balance += bet_amount
            cprint(f"You won 💲{bet_amount:.0f}!", Color.GREEN)
            display_balance(balance)

        elif (
            first_reel == second_reel
            or first_reel == third_reel
            or second_reel == third_reel
        ):
            bet_amount *= 2
            balance += bet_amount / 2
            cprint(f"You won 💲{bet_amount:.0f}!", Color.GREEN)
            display_balance(balance)

        else:
            balance -= bet_amount
            cprint(f"You lost!", Color.RED)
            display_balance(balance)

        if balance <= 0:
            cprint("You're out of money! Game over.", Color.RED)
            break

        continue_game = (
            input(
                colored("To play again press any key. To QUIT press 'q': ", Color.CYAN)
            )
            .lower()
            .strip()
        )
        if continue_game == GameConfig.QUIT:
            break
        continue


def main():
    """Entry point for the game"""
    cprint("👑👑👑 SLOT MASHINE GAME 👑👑👑\n", Color.YELLOW)
    balance = get_balance()
    cprint("\nWelcome to the Slot Mashine Game!", Color.GREEN)
    cprint(f"You start with a balance of 💲{balance:.0f}", Color.GREEN)
    play_game(balance)


if __name__ == "__main__":
    main()
