# This program is to guess the number name.

import random # to generate the random number

print('Hello, What is your name?')
name = input()

print('Well, ' + name + ' I am thinking of a number between 1 and 20')
secretnum = random.randint(1, 20)

for guessestaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretnum:
        print('Your guess is too low')
    elif guess > secretnum:
        print('Your guess is too high')
    else:
        break # this condition is for the correct guess

if guess == secretnum:
    print('Good job '+ name + '! You guessed my number in ' + str(guessestaken) + ' guesses')
else:
    print('Nope, The number I was thinking of was ' + str(secretnum))
    


