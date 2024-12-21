# In the file 'words.txt' we have a bunch of words
# Read from the file a list of words

from pathlib import Path

# Choose a random word
# While True:
# Print __________ (word)
# Take user guess
# If wrong input handle errors:
#   If len(guess) > 1:
#       Error message: Enter only one letter
#   If guess.isdigit()
#       Error message: Enter only letters from a to z.
#   If guess:
#       Check if guess in word.
#           Replace _ to guess (letter)
#   If wrong guess:


# =========================================================================
# print(f"3 {sentence.replace(' ', '')}")
# =========================================================================
#

# Start programm
#   Programm choose a random word from the list of words
#       from the file 'words.txt'

# astronaut
# _________
# _ _ _ _ _ _ _ _ _

# Enter a letter: abc
#   Error message: Enter only one letter
# Enter a letter: 1
#   Error message: Enter only letters from a to z.
# Enter a letter: a

# Good guess
# a_____a__

# Enter a letter: a
#   Error message: You already guessed that letter.

# Enter a letter: x
# Wrong guess
# a_____a__
#
# Enter a letter: x
#
# Maximmum of wrong attempts is 6
