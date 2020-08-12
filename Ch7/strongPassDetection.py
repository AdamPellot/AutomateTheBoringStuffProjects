#! python3
# strongPassDetection.py - Checks the strength of a password.
# Adam Pellot

import re


# Checks to see if password is strong.
def strongPass(password):

    # Character length regular expression.
    lengthRegex = re.compile(r'[a-zA-Z0-9]{8,}')
    mo = lengthRegex.search(password)
    if mo is None:
        print('This is not a strong password')
        return

    # At least one uppercase regular expression.
    upperCaseRegex = re.compile(r'[A-Z]+')
    mo = upperCaseRegex.search(password)
    if mo is None:
        print('This is not a strong password')
        return

    # At least one lowercase regular expression.
    lowerCaseRegex = re.compile(r'[a-z]+')
    mo = lowerCaseRegex.search(password)
    if mo is None:
        print('This is not a strong password')
        return

    # At least one digit regular expression.
    digitRegex = re.compile(r'\d+')
    mo = digitRegex.search(password)
    if mo is None:
        print('This is not a strong password')
        return

    print('This is a strong password')


# Asks user for a potential password string.
print('Please enter a potential password')
password = input()

strongPass(password)
