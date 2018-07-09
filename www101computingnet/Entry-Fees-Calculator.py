print('Start')
Adult_ticket = 15 #Fixed price
Child_ticket = 11 #Fixed price
print('The cost of each adult ticket is ' + str(Adult_ticket) + ' and cost of each child ticket is ' + str(Child_ticket))
try:
    adults = int(input('Enter the no of adult ticket(s): ')) #Reads input from user
    child = int(input('Enter the no of child ticket(s): ')) #Reads input from user

        
    #calculates the total cost of the user:
    total_cost = (Adult_ticket * adults) + (Child_ticket * child)

    #prints the total order amount of the customer:
    print('Your total amount for the ticket(s) is $' + str(total_cost))

    #Avail discount if the total cost is greater than $50:
    if total_cost > 50:
        discount = total_cost * 0.05 # 5 percent discount on total order
        final_cost = total_cost - discount # calculate the final cost, post discount
        print('Congrats, you availed a 5% discount on $' + str(total_cost) +  ' , please pay $' + str(final_cost) + ' as your final amount.')
    elif total_cost == 0:
        print('You have not choosen any tickets')
    else:
        print('Please pay $' + str(total_cost) + ' as your final amount.') # no discount, if price is less than $50
except ValueError:
        print('You entered a invalid value')

