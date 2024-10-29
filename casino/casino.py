from random import choice


def fruits_to_spin():
    choices = ("🍌", "🍎", "🍒")
    return choice(choices)


"""
def counter():
    count = 0

    def inner(value):
        nonlocal count
        count += value
        return count

    return inner
"""


def place_bets():
    while True:
        try:
            wallet = int(input("Place your bets:💲 ... "))
            print("Game started")
            print(f"You have {wallet}💲 on your account")
            return wallet
        except ValueError:
            print("Wrong input")


def game_over():
    STOP = "n"
    GO = "y"
    while True:
        game_over = input("Continue? (y/n): ").lower()
        if game_over == STOP:
            break

        else:
            wallet = place_bets()
    return wallet


def play():

    wallet = place_bets()

    while True:

        first = fruits_to_spin()
        second = fruits_to_spin()
        third = fruits_to_spin()
        game = (first, second, third)

        if wallet <= 0:
            print("Your wallet is empty! 😟")
            break

        elif first == second == third:
            print(f"{game} - You Win {wallet}💲")
            wallet *= 2
            print(f"You have {wallet}💲 on your account")

        else:
            print(f"{game} - Try again?")
            wallet -= 10
            print(f"You have {wallet}💲 on your account")

        game_over = input("To stop press 'S': ").lower()
        if game_over == "s":
            break


play()
