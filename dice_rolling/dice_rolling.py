from random import randint


def dices():
    dice_one = randint(1, 6)
    dice_two = randint(1, 6)
    return (dice_one, dice_two)


def game():

    while True:
        choice = input("Roll the dice? (y/n): ").lower().strip()

        if choice == "y":
            print(dices())
        elif choice == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")


game()
