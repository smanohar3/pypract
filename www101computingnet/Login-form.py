#A login form should ask the user to enter their username and password. It will then check if these login details are correct before displaying either a welcome message or an error message.
print('Start')
username = input('Enter username? ')
passcode = int(input('Enter Passcode? '))

if username != 'admin':
    print(username + ' is an invalid username')
if passcode != 1234:
    print(str(passcode) + ' is an invalid passcode')
else:
    print('You are logged in')
print('End')
