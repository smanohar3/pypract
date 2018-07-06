def collatz(number):
    
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
try:
    num = int(input("Give a number: "))
    while num != 1:
        num = collatz(int(num))
except:
    print('Enter a valid value')





    
    
    
