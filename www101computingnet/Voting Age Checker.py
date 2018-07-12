#Script to check the Voting Age.
#The user is prompted to enter the age, and the script check's if he/she
#is eligible to vote.

print('Start')
print('Let us check if you are eligible to vote?')
try: # Using 'try' and 'catch' to handle exceptions.
    age = int(input('Enter your age: '))
    if age < 0: # Age can't be negative.
        raise ArithmeticError
    if len(str(age)) > 3: # Age can't be more than 3 character's.
        print('Recheck the age and enter again.')
    elif age >= 18: # Checking if the age is more than 18
        print('You are eligible to vote.')
    else:
        gap = 18 - age # Calculating the gap if the age is less than 18
        print('You will be able to vote in ' + str(gap) + ' years.')
    
except ValueError: # Exception raised, to handle non numerical value.
    print('You have entered an invalid value.')

except ArithmeticError: # Exception raised, to handle negative value.
    print('Age cannot be a negative value.')


