"""
Bugs fixed:
1. The if statement is comparing a string to an integer.
2. There should be another toss RNG at the 2nd guess.
3. There is a misspelled variable name 'guesss' in the else statement.
"""

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
toss = 'heads' if toss == 1 else 'tails'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    toss = random.randint(0, 1)  # 0 is tails, 1 is heads
    toss = 'heads' if toss == 1 else 'tails'
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
