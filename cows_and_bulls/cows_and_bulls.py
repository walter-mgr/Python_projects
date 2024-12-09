# Generate a random 4-digit number
# Print a message: Try to guess a 4-digit number with unique digits.
# # Take user input
# # Give a feddback
import random


def get_four_unique_digit_number():
    digits = random.sample(range(10), 4)
    return "".join([str(digit) for digit in digits])


secret_number = get_four_unique_digit_number()
print(secret_number)


"""
#   When run a program computer generates a 4-digit number with unique digits
#   User need to guess a number with the computer hints

    # Get valid input:
        # Not an integer, not a string, not a double or tripple digits

    #  Guess: 1123
    #  Invalid guess. Please enter a 4-digit number with unique digits.
    
    #  Guess: 1234
        2 cows, 1 bulls / one of the digits is in the correct position
                          two digits that a right, but in the wrong position

    #  Guess: 4321
        3 cows, 0 bulls / 0 of the digits on the correct position

    #  Guess: 4231
        2 cows, 1 bulls

    #  Guess: 1243
        0 cows, 3 bulls

    #  Guess: 4321
        2 cows, 1 bulls

    #  Guess: 4321
        0 cows, 3 bulls

    #  Guess: 9321
        0 cows, 4 bulls
    
                        
"""
