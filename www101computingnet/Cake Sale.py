#Script to calculate the total amount raised for the cup cakes sales:

print('Start.')
print('The cost of cake(s) types is as follows:\n'
      'CupCakePrice:   40 paise\n'
      'MacaronsCakePrice:   50 paise\n'
      'CheeseCakePrice: 70 paise\n')

#The cost is fixed for the following:
CupCakePrice = 0.40          
MacaronsCakePrice = 0.50
CheeseCakePrice = 0.70
expenses = 0.12

#Adding exceptions to handle the input values i.e strings(e.g. 'asasas') /negative numbers(e.g. -9)/invalid numbers like(e.g.111112121 etc)
try:
    cupcakes = int(input('How many CupCakes would you like to sell?: '))  #reads the input from user.
    if cupcakes < 0 or len(str(cupcakes)) > 3: #validating if the value is less than zero or checking the length of the string entered.
        raise ArithmeticError
    cupcakescost = cupcakes * CupCakePrice     #calculates the cost of the cake 
    print('The total cost of CupCakes is $' + str(round(cupcakescost,2)))

    macronscake = int(input('How many MacaronsCake would you like to sell?: ')) #reads the input from user.
    macronscakecost = macronscake * MacaronsCakePrice #calculates the cost of the cake
    print('The total cost of MacaronsCake is $' + str(round(macronscakecost,2)))

    cheesecake = int(input('How many CheeseCake would you like to sell?: ')) #reads the input from user.
    cheesecakecost = cheesecake * CheeseCakePrice #calculates the cost of the cake
    print('The total cost of CheeseCake is $' + str(round(cheesecakecost,2)))

    totalCost = cupcakescost + macronscakecost + cheesecakecost #calculates the total cost of the cakes
    print('The final cost of your order is $' + str(round(totalCost,2)))

    profit = totalCost - expenses  #checking the profit.
    if profit > 0:
        print('The profit incurred on $' + str(round(totalCost,2)) + ' is ' + str(round(profit,2)))
    else:
        print('You incurred loss on this $' + str(round(totalCost,2)))

except ValueError:  #handles the error if the user enters the string.
    print('The value entererd is not a valid value.')
except ArithmeticError: #handles the error if the user enters the negative numbers.
    print('Please recheck the value that you have entered.')
print('End.')

