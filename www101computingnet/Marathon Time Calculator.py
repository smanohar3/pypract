#Marathon Time Calculator
print('Start')

str_pace = input('Enter the pace at which you can run[e.g. 5:25]: ')
split_pace = str_pace.split(":")
minutes = int(split_pace[0])
seconds = int(split_pace[1])
pace = minutes * 60 + seconds

totalTime = pace * 42
hours = totalTime // 3600
timeLeft = totalTime % 3600

minutes = timeLeft // 60
seconds = timeLeft % 60
print("You should complete the marathon in " + str(hours) + ":" + str(minutes) + ":" + str(seconds)+ "!")
print('End')


