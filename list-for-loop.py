Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(0, 10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(0, 10, 2):
	print('The first value is ' + i)

	
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    print('The first value is ' + i)
TypeError: must be str, not int
>>> for i in range(0, 10, 2):
	print('The first value is ' + str(i))

	
The first value is 0
The first value is 2
The first value is 4
The first value is 6
The first value is 8
>>> The first value is 2
SyntaxError: invalid syntax
>>> 
>>> list(range(4))
[0, 1, 2, 3]
>>> 
>>> 
>>> list(range(0, 100, 2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> 
>>> 
>>> 
>>> 
>>> supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
>>> for i in range(len(supplies)):
	print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders
>>> 
>>> 
>>> 
>>>  supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
SyntaxError: unexpected indent
>>> supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
>>> for i in supplies:
	print(i)

	
pens
staplers
flame-throwers
binders
>>> 
>>> 
>>> list(range(0, 100, 2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> spam = list(range(0, 100, 2))
>>> spam
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> 
>>> 
>>> 
>>> supplies = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', ]
>>> for i in supplies:
	print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

	
Traceback (most recent call last):
  File "<pyshell#42>", line 2, in <module>
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
TypeError: list indices must be integers or slices, not str
>>> for i in range(len(supplies)):
	print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

	
Index 0 in supplies is: pens
Index 1 in supplies is: pens
Index 2 in supplies is: pens
Index 3 in supplies is: pens
Index 4 in supplies is: pens
Index 5 in supplies is: pens
Index 6 in supplies is: pens
Index 7 in supplies is: pens
>>> 
>>> 
>>> 
>>> 
>>> 
>>> cat = ['fat', 'orange', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> voice = cat[2]
>>> 
>>> 
>>> 
>>> size, color, voice = cat
>>> size
'fat'
>>> color
'orange'
>>> voice
'loud'
>>> 
>>> 
>>> size, color, voice = 'lean', 'black', 'quiet'
>>> a = 'AAA'
>>> b = 'BBB'
>>> b = a
>>> a, b = b, a
>>> a
'AAA'
>>> a = 'AAA'
>>> b = 'BBB'
>>> a, b = b, a
>>> b
'AAA'
>>> a
'BBB'
>>> 
>>> 
>>> 
>>> 
>>> spam = 42
>>> spam + 1
43
>>> spam = spam + 1
>>> spam += 1
>>> spam
44
>>> spam = 42
>>> spam += 1
>>> spam
43
>>> spam -= 1
>>> spam
42
>>> spam *= 2
>>> spam
84
>>> spam %= 2
>>> spam
0
>>> spam /= 1
>>> spam
0.0
>>> 
>>> 
>>> 
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hello')
0
>>> 
>>> spam.index('heyas')
3
>>> spam.index('asasasas')
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    spam.index('asasasas')
ValueError: 'asasasas' is not in list
>>> spam = ['hello', 'hi', 'howdy', 'hi']
>>> spam.index('hi')
1
>>> spam = ['cat', 'dog', 'bat']
