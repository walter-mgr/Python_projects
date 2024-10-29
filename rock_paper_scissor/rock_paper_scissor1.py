from random import choice

emojis = {"r": "🪨", "p": "📜", "s": "✂️"}
choices = ("r", "p", "s")


def display_choices(your_choice, computer_choice):
    print(f"You chose: {emojis[your_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")


def get_user_choice():
    while True:
        your_choice = input("Rock, paper or scissors? (r|p|s): ").lower()
        if your_choice in choices:
            return your_choice
        else:
            print("Invalid choice!")


def determine_winner(your_choice, computer_choice):
    if your_choice == computer_choice:
        print("Tie!")
    elif (
        (your_choice == "r" and computer_choice == "s")
        or (your_choice == "s" and computer_choice == "p")
        or (your_choice == "p" and computer_choice == "r")
    ):
        print("You win!")
    else:
        print("You lose!")


def play_game():
    while True:
        your_choice = get_user_choice()

        computer_choice = choice(choices)

        display_choices(your_choice, computer_choice)

        determine_winner(your_choice, computer_choice)

        game_over = input("Continue? To stop press 'n': ").lower()
        if game_over == "n":
            break


if __name__ == "__main__":
    play_game()

"""
while True:
    computer_choice = choice(choices)

    your_choice = input("Rock, paper or scissors? (r|p|s): ").lower()
    if your_choice not in choices:
        print("Invalid choice!")
        continue

    elif your_choice == computer_choice:
        print("Tie!")
        continue
    elif (
        (your_choice == "r" and computer_choice == "s")
        or (your_choice == "s" and computer_choice == "p")
        or (your_choice == "p" and computer_choice == "r")
    ):
        print_emoji()
        print("You win!")
    else:
        print_emoji()
        print("You lose!")
    game_over = input("Continue? To stop press 'n': ").lower()
    if game_over == "n":
        break
"""
