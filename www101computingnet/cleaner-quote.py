#Script to calculate the quote for cleaning the windows:
#The user enters the number of windows to be cleaned and the
#script displays the cost to clean those.

print('Start.')

#QuotePrice is Fixed
QuotePrice = 10
#For First Five windows cost:
FirstFive = 2
#Between Five to Ten windows cost:
FiveToTen = 1.50
#Above Ten windows cost:
TenAbove = 1

#Handles exceptions:
try:
    #Reads input from user(s) - only numbers
    NumOfWindows = int(input('How many windows need to be cleaned? '))
    #no negative numbers and invalid number of integers.
    if NumOfWindows <= 0 or len(str(NumOfWindows)) > 2:
        raise ArithmeticError
    #if the number of windows up to 5
    if NumOfWindows <= 5:
        cost = QuotePrice + (NumOfWindows * FirstFive)
        print('The cost of cleaning ' + str(NumOfWindows) + ' windows is $' + str(cost))
    #Between 6 and 10 windows:    
    elif NumOfWindows >= 6 or NumOfWindows <= 10:
        cost = QuotePrice + (NumOfWindows * FiveToTen)
        print('The cost of cleaning ' + str(NumOfWindows) + ' windows is $' + str(cost))
    #Above 10 windows:
    elif NumOfWindows > 10:
        cost = QuotePrice + (NumOfWindows * TenAbove)
        print('The cost of cleaning ' + str(NumOfWindows) + ' windows is $' + str(cost))
    
except ValueError: # Exception raised, to handle non numerical value.
    print('You have entered an invalid value.')
    
except ArithmeticError:
    print('Please check the input value.')

    
print('End.')

