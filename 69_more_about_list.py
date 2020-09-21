# More about list

# generate lists with range functions
# something more about pop method
# index method
# pass list to a function


# numbers = list(range(1,11))
# print(numbers)
# numbers.pop()
# print(numbers)


# if i found perticular element position
# print(numbers.index(1))

# if list has two 1 then
# syntax: numbers.index(value to be find, start searching position, stop searching position)
# print(numbers.index(3,2))

# pass list inside function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))