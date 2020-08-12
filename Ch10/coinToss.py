#! python3
# coinToss.py - Debug coin toss from Automate the Boring Stuff .
# Adam Pellot

import random

guess = ''

# Ensures Heads and Tails will also be accepted as answers.
while guess.lower() not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

# Links 1 and 0 to heads and tails respectively so toss can be compared
# to guess on line 23
if guess.lower() == 'heads':
    guess = 1
else:
    guess = 0

toss = random.randint(0, 1)  # 0 is tails, 1 is heads.

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    # Mispelling: Changed from guesss to guess.
    guess = input()
    # Ensures no problems with second guess.
    while guess.lower() not in ('heads', 'tails'):
        print('Enter either heads or tails:')
        guess = input()
    if guess.lower() == 'heads':
        guess = 1
    else:
        guess = 0
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
