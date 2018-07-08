#Script that calculates the age from today up to 50 Years:
print('Hey!!!')
Year = 2018 #hard coded. we can use datetime to make it dynamic
Age = int(input('How old are you now in ' + str(Year) + '?   '  ))

for i in range(1, 50):
    Year = Year + 1
    Age = Age + 1
print('In ' + str(Year) + ' you will be ' + str(Age) + ' years old.')


