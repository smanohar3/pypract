#Python script that prompts the user to enter a
#discounted price (e.g. $90) and the discount rate
#that this price benefits from (e.g. 25%)
#The program will then calculate and display the original price
#(price before discount) of the item (e.g. $120).

discountedPrice = int(input('Discounted price?: $ '))

discount = int(input('Percentage Discount(%): '))

originalPrice = round(discountedPrice/(1-discount/100),2)

print('The originalPrice was $ ' + str(originalPrice))



