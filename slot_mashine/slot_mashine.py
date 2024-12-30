import random


class GameConfig:
    QUIT = "q"


# Get reels
def get_reel():
    reels = ("🍌", "🍑", "🍒")
    return random.choice(reels)


# Ask user for valid starting balance
def get_balance():
    pass


# Ask user for valid bet amount
def get_bet_amount():
    pass


# Invite and greet the user to start the game
# Run game logic
def play_game():
    pass


def main():
    get_reel()


if __name__ == "__main__":
    main()

# Define variables:

#   #    ballance
#   #    bet_amount
#   #    expence
#   #    income
#   #    reels


""" Slot Mashine Game

# Enter your starting balance: $a
#   If not a number: Please enter a valid number.

# Enter your starting balance: $0 or -1
#   If < 0: Balance must be a positive number.

# Enter your starting balance: $100

# Welcome to the Slot Mashine Game!
# You start with a balance of $100.

# Current balance: $100
# Enter your bet amount: $a
#   If not: Please enter a valid number for the bet amount.

# Enter your bet amount: $ if 0 > bet_amount > balance ($200)
#   Invalid bet amount. You can bet between $1 and $100 {balance}

# 💲call emojies: WINDOWS + .

# Enter your bet amount: $10
# 🍒 | 🍑 | 🍌
# You lost!
# Do you want to play again? y/n:

# Current balance: $90
# Enter your bet amount: $10
# 🍒 | 🍌 | 🍌
# You won $20!
# Do you want to play again? y/n:


# =================================================================
#  # If two symbols match, the payout is two times the bet amount. 10 x 2 = $20
# =================================================================
#  # If three symbols match, the payout is ten times the bet amount. 10 x 10 = $100
# =================================================================
#  # If current balance == 80:
#  #    $20 - income
#  #    $10 - expence
#  #    20 - 10 = 10 difference
#  #    current ballance + difference: 80 + 10 = 90
#  #    current ballance + (income - expence): 80 + (20 - 10) = 90

# Current balance: $100
# Enter your bet amount: $100
# 🍒 | 🍑 | 🍌
# You lost!
# You are out of money! Game over.

"""
