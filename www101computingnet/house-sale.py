#This program is used to store various characteristics of a house
#and show the full description of the house.

#Fixed Variables
StreetName = "Turing Street"
City = "London"
TypeOfHouse = "Semi-detached"
Bedrooms = "Three"
Reception = "Two"
Floors = "Two"
Sale = "1,000,000"

print('#########################')
print('#                       #')
print('#       FOR SALE        #')
print('#                       #')
print('#########################')
print("A superb " + TypeOfHouse + " house located on\n"
      + StreetName + '.' + "This house contains \n" + Bedrooms
      + ' bedrooms' + ' and ' + Reception + " reception rooms and is organized across \n"
      + Floors + " floors." + " It is for sale at $" + Sale +'.')

