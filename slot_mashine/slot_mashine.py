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
- Messages: Contains various string constants used throughout the game.
- MultiplyIfMathch: Contains constants that define the multipliers for winnings when
    two or more symbols are matched. These multipliers are used to calculate the
    total winnings based on the bet amount.

Functions:
- display_balance(balance): Displays current user's balance.
- spin_reels(reels): Simulates slot machine spinning reels. Returns a tuple with
    three random symbols.
- display_reels(first, second, third): Displays symbols.
- get_balance(): Prompts userto enter a valid starting balance.
- get_bet_amount(balance): Prompts user to enter a valid bet amount.
- display_winnings(amount): Displays the amount the player won.
- update_balance_win(balance: int, bet_amount: int, multiplier: int): Updates the
    balance when player wins.
- update_balance_loss(balance: int, bet_amount: int): Updates balance when player loses.
- calculate_current_balance(first_reel: str, second_reel: str, third_reel: str,
    balance:int, bet_amount: int): Calculates the current balance based on the
        outcome of the reels.
- play_again(): Prompts user to continue game. Returnes user's choice.
- play_game(balance): Main game loop that handles game play.
- main(): Entry point for the game
"""

import random
from termcolor import cprint, colored


class GameConfig:
    QUIT = "q"
    REELS = ("🍌", "🍑", "🍒", "🍋", "🥝")
    REELS_NUMBER = 3
    MIN_BALANCE = 1


class MultiplyIfMatch:
    MATCH_TWO = 2
    MATCH_THREE = 10
    # Future multipliers (currently in development)
    # MATCH_FOUR = 15
    # MATCH_FIVE = 20


class Color:
    CYAN = "cyan"
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"


class Messages:
    BALANCE_PROMPT = "Enter your starting balance: 💲"
    BET_PROMPT = "Enter your bet amount: 💲"
    INVALID_BALANCE = "Balance must be a positive number."
    INVALID_BET = "Invalid bet amount. You can bet between 💲1 and 💲{balance}"
    VALID_NUMBER = "Please enter a valid number."
    WIN = "You won 💲{amount:.0f}!"
    LOST = "You lost!"
    CONTINUE = "To play again press any key. To QUIT press 'q': "
    GAME_OVER = "You're out of money! Game over."
    GAME_TITLE = "👑👑👑 SLOT MACHINE GAME 👑👑👑\n"
    WELCOME = "\nWelcome to the Slot Machine Game!"
    START_BALANCE = "You start with a balance of 💲{balance:.0f}"
    CURRENT_BALANCE = "\nCurrent balance: 💲{balance:.0f}"


def display_balance(balance: int) -> None:
    """Displays current user's balance."""
    cprint(Messages.CURRENT_BALANCE.format(balance=balance), Color.YELLOW)


def spin_reels(reels: tuple) -> tuple:
    """Simulates slot mashine spinning reels. Returns a tuple with three random symbols."""
    return tuple(random.choice(reels) for _ in range(GameConfig.REELS_NUMBER))


def display_reels(first: str, second: str, third: str) -> None:
    """Displays symbols."""
    print(f"{first} | {second} | {third}")


def get_balance() -> int:
    """Prompts user to enter a valid starting balance."""
    while True:
        try:
            balance = int(input(colored(Messages.BALANCE_PROMPT, Color.CYAN)))
            if balance < GameConfig.MIN_BALANCE:
                cprint(Messages.INVALID_BALANCE, Color.RED)
            else:
                return balance
        except ValueError:
            cprint(Messages.VALID_NUMBER, Color.RED)


def get_bet_amount(balance: int) -> int:
    """Prompts user to enter a valid bet amount."""
    while True:
        try:
            bet_amount = int(input(colored(Messages.BET_PROMPT, Color.CYAN)))
            if bet_amount < GameConfig.MIN_BALANCE or bet_amount > balance:
                cprint(
                    Messages.INVALID_BET.format(balance=balance),
                    Color.RED,
                )
            else:
                return bet_amount
        except ValueError:
            cprint(Messages.VALID_NUMBER, Color.RED)


def display_winnings(amount: int) -> None:
    """Displays the amount the player won."""
    cprint(Messages.WIN.format(amount=amount), Color.GREEN)


def update_balance_win(balance: int, bet_amount: int, multiplier: int) -> int:
    """Updates the balance when player wins."""
    winnings = bet_amount * multiplier - bet_amount
    balance += winnings
    display_winnings(winnings)
    return balance


def update_balance_loss(balance: int, bet_amount: int) -> int:
    """Updates balance when player loses."""
    balance -= bet_amount
    cprint(Messages.LOST, Color.RED)
    return balance


def calculate_current_balance(
    first_reel: str, second_reel: str, third_reel: str, balance: int, bet_amount: int
) -> int:
    """Calculates the current balance based on the outcome of the reels."""
    if first_reel == second_reel == third_reel:
        balance = update_balance_win(balance, bet_amount, MultiplyIfMatch.MATCH_THREE)

    elif (
        first_reel == second_reel
        or first_reel == third_reel
        or second_reel == third_reel
    ):
        balance = update_balance_win(balance, bet_amount, MultiplyIfMatch.MATCH_TWO)

    else:
        balance = update_balance_loss(balance, bet_amount)
    return balance


def play_again() -> str:
    """Prompts user to continue game. Returnes user's choice."""
    return input(colored(Messages.CONTINUE, Color.CYAN)).lower().strip()


def play_game(balance: int) -> None:
    """Main game loop that handles game play."""
    while balance >= GameConfig.MIN_BALANCE:
        display_balance(balance)
        bet_amount = get_bet_amount(balance)
        first_reel, second_reel, third_reel = spin_reels(GameConfig.REELS)
        display_reels(first_reel, second_reel, third_reel)

        balance = calculate_current_balance(
            first_reel, second_reel, third_reel, balance, bet_amount
        )

        display_balance(balance)

        if balance < GameConfig.MIN_BALANCE:
            cprint(Messages.GAME_OVER, Color.RED)
            break

        continue_game = play_again()
        if continue_game == GameConfig.QUIT:
            display_winnings(balance)
            break


def main():
    """Entry point for the game"""

    cprint(Messages.GAME_TITLE, Color.YELLOW)
    balance = get_balance()
    cprint(Messages.WELCOME, Color.GREEN)
    cprint(Messages.START_BALANCE.format(balance=balance), Color.GREEN)
    play_game(balance)


if __name__ == "__main__":
    main()
