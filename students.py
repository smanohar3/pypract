#Script that validates if he/she eligible for entrance test
#to pursue higher studies.
#Min marks required:

#Percentage of marks required to appear for test
Graduation = 60
Twelth = 70
Tenth = 70
try:
    Percent = int(input('Please enter your Graduation(%): '))
    if len(str(Percent)) > 2:
        raise ArithmeticError

    TwelthPercent = int(input('Please enter your Twelth(%): '))
    TenthPercent = int(input('Please enter your Tenth(%): '))
    
    if (Percent  > TenthPercent or Percent > TwelthPercent) and (Percent > Graduation):
        print('You qualify to take up the entrance test. Good Luck')
    else:
        print('Oops, You cannot take up the written test')
except ArithmeticError:
    print('Please check the value that you have entered.')
except ValueError:
    print('Percentage Value cannot be character(s)')
    


    




