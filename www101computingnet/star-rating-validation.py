#The aim of this Python challenge is to validate a user input using a range check.
#In this program, the user will be asked to enter a star rating by entering a number value between 0 and 5. This could for instance be used to rate a movie (5 Stars = Excellent , 0 Star = Disappointing).
print('Start')
try:
    StarRating = int(input('Enter a rating from [0 to 5] : '))

    if StarRating < 0:
        print('Rating can''t be ' + str(StarRating) +  ' ,' + ' Please try again.')
    elif StarRating > 5:
        print('Rating can''t be ' + str(StarRating) + ' ,' + ' Please try again.')
    else:
        print('Thanks for the rating ' + str(StarRating) + ' :) ')
except ValueError:
    print('Oops, Rating can''t be a string :( ! Please enter a valid value')

print('End')

