#The program will then display the full multiplication table, from 1 to 10, for the number entered by the user.
print('Start')
number = int(input('Enter the number: '))
for i in range(1, 11):
    product = number * i
    print(str(number) + ' x ' + str(i) + ' = ' + str(product))
print('End')
