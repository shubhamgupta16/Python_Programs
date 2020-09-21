# function returning two values in tuple format
def func(int1, int2):
    add = int1 + int2
    multiply = int1 * int2
    return add, multiply

# print(func(2,3))
# or 
var1, var2 = func(2,3)
print(var1)
print(var2)