#Script for Time Conversion - from 24-hour to 12-hour clock convertor.

print('Start')

time = input('Enter a time in [12 hour clock or 24 hour clock] in the format of HH:MM -  ')
hours = int(time[0:2])
minutes = time[-2:]

if hours == 0:
    hours = 12
    print(str(hours) + '.' + str(minutes) + ' am')
elif hours < 12:
    print(str(hours) + ':' + str(minutes) + ' am')
elif hours == 12:
    print('The time in 12 hour clock is ' + str(hours) + ':' + str(minutes) + ' pm')
elif hours < 24:
    hours = hours - 12
    print('The time in 12 hour clock is ' + str(hours) + ':' + str(minutes) + ' pm')

print('end')

    

