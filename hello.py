# This program says hello and asks for my name

print('Hello world!')

print('What is your name?') # ask for their name
myname = input()
print('It is good to meet you, ' + myname)

print('What is your age?') # ask for their age
myage = input()
print('You will be ' + str(int(myage) + 1) + ' in a year :) ')

print('The length of your name is:')
print(len(myname))

#print('What is your age?') # ask for their age
#myage = input()
#print('You will be ' + str(int(myage) + 1) + 'in a year.')

print('What are your hobbies ' + myname + '?')
myhobbies = input()
print(' That''s good to hear, ' + myhobbies + ' I love the same ')

print('Where do you work ' + myname + '?')
mywork = input()
print('I heard ' + mywork + ' is a great place to work, Lucky you! ')



