#Script to check if an year is a leap year or not:
print('Start')
year = int(input('Enter the year for which you want to check, \nif it is a leap year or not? : ' ))

if len(str(year)) > 4:
    print('oops, the value you entered ' + str(+year) + ' is an invalid value')
elif year % 4 == 0:
    print(str(+year) + ' is a leap year')
else:
    print(str(+year) +' is not a leap year')

    
    
 




