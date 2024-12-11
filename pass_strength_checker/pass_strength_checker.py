""" Password Strength Checker

This program evaluates the strength of a given password based on predefined criteria:
1. Very Weak
2. Weak
3. Medium
4. Strong
5. Very Strong

The program uses regex patterns to assess the password strength and categorizes
it accordingly.

Password Strength Criteria:
- Very Weak: 4 digits
- Weak: 8 digits
- Medium: 8 digits with at least one uppercase letter
- Strong: More than 6 characters with at least one uppercase and one lowercase letter
- Very Strong: More than 5 characters with at least one uppercase letter, one lowercase letter, and at least one special symbol

User Input:
- The user is prompted to enter a password.
- The program then evaluates and prints the strength of the password.

"""

import re


strength_criteria = {
    "Very Strong": r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*(),.?:{}|<>]).{5,}$",
    "Strong": r"^(?=.*[A-Z])(?=.*[a-z]).{6,}$",
    "Medium": r"^(?=.*[A-Z]).{7,}$",
    "Weak": r"^\d{8}$",
    "Very Weak": r"^\d{4}$",
}


def check_password_strength(password: str, strength_criteria: dict) -> str:
    for strength, pattern in strength_criteria.items():
        if re.match(pattern, password):
            return strength
    return "Very Weak"


def main():
    while True:
        password = input("Enter a password: ")
        strong_pass = check_password_strength(password, strength_criteria)
        if strong_pass == "Very Strong":
            print(f"Your password is {strong_pass}")
            break
        print(f"Your password is {strong_pass}")


if __name__ == "__main__":
    main()


# Create a regex pattern for checking the password strength

# Take user input: Enter a password: 1234
#   # If input is 4 digits
#       # Very week
#   # If input is 8 digits
#       # Week
#   # If input is 8 digits and Uppercase Letter
#       # Medium
#   # If input is > 6 digits and Uppercase and Lowercase letter
#       # Strong
#   # If input is > 5 digits and Uppercase and Lowercase and >= 1 special symbol
#       # Vrey strong
