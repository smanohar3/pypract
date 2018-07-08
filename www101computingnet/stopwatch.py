#Our stopwatch algorithm will convert/format this number of seconds to calculate and display the matching number of hours, minutes and seconds, knowing that:
#Script for an example of Sequence Algorithm:
print('Start')
number = int(input('Enter a number (seconds): ' ))
hours = number // 3600
remainder = number % 3600
minutes = remainder // 60
seconds = remainder % 60
print(str(number) + ' seconds =  ' + str(hours) + ' hours, ' + str(minutes) + ' minutes ' +  str(seconds) + ' seconds')
print('End')

