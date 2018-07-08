#Winter Olympics take place every 4 years. So when would be the next winter Olympics?
#Script used to display the dates of the next ten Winter Olympics.
#Iteration
print('Start')
winter_olympics = int(input('Enter the year: '))
for i in range(1, 11):
    winter_olympics = winter_olympics + 4
    print('The next winter olympics will be held in ' + str(winter_olympics))


