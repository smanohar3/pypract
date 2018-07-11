#Script to calculate the Discount Price Calculator.
#Python script that prompts the user to enter a price(ex: $90),
#and a discount rate to apply (ex: 20%)
#Program will then calculate and display the discounted price.

print('Start') #program starts
try:           #Adding exceptions (try) and (catch) to restrict the user to input only numericals.
    Price = int(input('Enter the price of your item, [e.g. 60]: '))
    if Price <= 0 or len(str(Price)) > 4: 
        raise ArithmeticError
    DiscountRate = int(input('Enter the percentage discount, [e.g. 10]: '))
    Discount = (Price * DiscountRate / 100)
    DiscountPrice = Price - Discount
    
    print('Price before discount = ' + str(Price))
    print('Discount rate = ' + str(DiscountRate) + str('%'))
    print('Discount = $' + str(Discount))
    print('Price after discount = $' + str(DiscountPrice))
except ValueError:
    print('Oops, Invalid Value is entered, Please check the input.')
except ArithmeticError:
    print('The number was not positive or you have entered 0 or you must have\n'
           'entered an invalid number, Please try again.')


print('End') #program ends
