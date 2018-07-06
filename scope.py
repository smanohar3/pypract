#local scope
def spam():
    eggs = 23
    print(eggs)

spam()

#global scope
def spam_1():
    eggs = 27
    print(eggs)

spam_1()
eggs = 21
print(eggs)
