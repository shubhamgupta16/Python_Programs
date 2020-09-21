# Scope of variable inside and outside function

x = 5 # global variable


def func():
    global x # this define that inside this function i use global x meanse here at this point value of x is 5 after this line value is change to 7 globally
    x = 7 # local variable
    return x

print(x)
print(func())
print(x)