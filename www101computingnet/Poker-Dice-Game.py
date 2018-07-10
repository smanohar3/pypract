#Poker Dice Game:
#The computer will generate three random numbers between 1 and 6.
#The program will then check to see if the three dice have the same value (“Three of a kind!”) or if any two of the three dice have the same value (“Pair”).
#This algorithm is a good example of: Selection

print('Start') #program begins

import random # import random module to generate random no's
die1 = random.randint(1, 6) # generating randon no's from 1 - 6
die2 = random.randint(1, 6)
die3 = random.randint(1, 6)
print('die1: ' + str(die1)) # printing the random no of die 1
print('die2: ' + str(die2)) # printing the random no of die 2
print('die3: ' + str(die3)) # printing the random no of die 3

if (die1 == die2 and die2 == die3): #checking if all the three die rolled have same number
        print('Three of a kind')
elif (die1 == die2 or die2 == die3 or die1 == die3): #checking if any of the two die rolled have same number.
    print('1 Pair')
else:
    print('Better luck, next time') #checking if none of the three die rolled have same number.

print('End') #program ends


            



    

