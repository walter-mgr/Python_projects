from random import choice


def choices():
    print(f"Your choice: {your_choice}")
    print(f"Computer choice: {computer_choice}")


while True:
    computer_choice = choice(["r", "p", "s"])
    your_choice = input("Rock, paper or scissors? (r|p|s): ").lower()

    if your_choice == "r" or your_choice == "p" or your_choice == "s":

        if (
            (your_choice == "r" and computer_choice == "s")
            or (your_choice == "s" and computer_choice == "p")
            or (your_choice == "p" and computer_choice == "r")
        ):
            choices()
            print("You win!")
            game = input("Continue? (y|n): ").lower()
            if game == "y":
                continue
            elif game == "n":
                break
            else:
                print("Invalid input!")

        elif (
            (your_choice == "r" and computer_choice == "p")
            or (your_choice == "p" and computer_choice == "s")
            or (your_choice == "s" and computer_choice == "r")
        ):
            choices()
            print("You lose!")
            game = input("Continue? (y|n): ").lower()
            if game == "y":
                continue
            elif game == "n":
                break
            else:
                print("Invalid input!")

        elif your_choice == computer_choice:
            continue
        else:
            break

    else:
        print("Invalid input!")
