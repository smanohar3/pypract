print('Enter your name?')
#Reads the user's name:
myName = input()

print('Hi ' + myName+' ,' + ' Let us calculate the area, perimeter(if applicable) for the follwing figures: viz \n Square, Rectangle, Circle, Triangle, Parallelogram, Rhombus etc.')

#Reads the user's input:
Name = input('Enter the value from the above: ')

#Square:
if Name == 'square':
    side = int(input('Enter the side of ' + Name + ' : '))
    Area_square = side  ** 2
    Perim_square = 4 * side
    print('The area of the ' + str(Name) + ' is ' + str(Area_square))
    print('The perimeter of the ' + str(Name) + ' is ' + str(Perim_square))
#Rectangle:
elif Name == 'rectangle':
    length = int(input('Enter the length of ' + Name + ' : '))
    breadth = int(input('Enter the breadth of ' + Name + ' : '))
    Area_rect = length * breadth
    Perim_rect = 2 * (length + breadth)
    print('The area of the ' + str(Name) + ' is ' + str(Area_rect))
    print('The perimeter of the ' + str(Name) + ' is ' + str(Perim_rect))
#Circle:
elif Name == 'circle':
    radius = int(input('Enter the radius of ' + Name + ' : ' ))
    Area_circ = 3.14 * radius ** 2
    Perim_circ = round(2 * 3.14 * radius, 2)
    print('The area of the ' + str(Name) + ' is ' + str(Area_circ))
    print('The perimeter of the ' + str(Name) + ' is ' + str(Perim_circ))
#Triangle:
elif Name == 'triangle':
    base = int(input('Enter the base of ' + Name + ' : '))
    height = int(input('Enter the height of ' + Name + ' : '))
    side = int(input('Enter the side: ' ))
    Area_tria = (base * height)/2
    Perim_tria = (base + height + side)
    print('The area of the ' + str(Name) + ' is ' + str(Area_tria))
    print('The perimeter of the ' + str(Name) + ' is ' + str(Perim_tria))
#Parallelogram:
elif Name == 'parallelogram':
    base = int(input('Enter the base of ' + Name + ' : '))
    height = int(input('Enter the height of ' + Name + ' : '))
    Area_para = base * height
    print('The area of the ' + str(Name) + ' is ' + str(Area_para))
#Rhombus:
elif Name == 'rhombus':
    p_diagnol = int(input('Enter the diagnol 1 of ' + Name + ' : '))
    q_diagnol = int(input('Enter the diagnol 2 of ' + Name + ' : '))
    Area_rhom = (p_diagnol * q_diagnol)/2
    print('The area of ' + str(Name) + ' is ' + str(Area_rhom))
else:
    print('Please enter a valid value')
