#Script which reads an input from user and converts the
#temperature in to C - F or F - C scale.
#Selection Algorithm Example:
print('Start')
print('Temperature Converter - Main Menu')
print('1- Convert from Celsuis to Fahrenheit') # Reads the option 1 or 2 
print('2- Convert from Fahrenheit to Celsuis') 

try:
    option = int(input('Choose an option - 1 or 2: ')) # takes input from user.
    if option == 1: #Check it the option is '1'
        Celsuis = int(input('Type a temperature in Degrees Celsuis: '))
        Fahrenheit = (Celsuis * 9/5) + 32 # converts from Celsius to Fahrenheit.
        print('Temperature ' + str(Fahrenheit) + ' Degrees Fahrenheit')
    elif option == 2: #Check it the option is '2'
        Fahrenheit = int(input('Type a temperature in Degrees Fahrenheit: '))
        Celsuis = (Fahrenheit - 32) * 5/9 # converts from Fahrenheit to Celsius.
        print('Temperature ' + str(Celsuis) + ' Degrees Celsuis')
    else:
        print('Invalid option.') # if none of the options 1 or 2 entered

except ValueError: # exception raised, when non numericals are entered.
    print('Invalid option.') 
