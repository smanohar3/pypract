print('How many dogs do you have?')
numDogs = input()
try:
    if int(numDogs) >= 4:
        print('That is a lot of dogs')
    elif int(numDogs) < 0:
        print('Enter a valid number')
    else:
        print('That is not many dogs')
except:
    print('You did not enter a number')
