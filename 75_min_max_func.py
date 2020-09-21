# min and max function

numbers = [6,60,2]
# print(min(numbers))
# print(max(numbers))

# make a program using max and min to find the difference of max and min number

def greatest_diff(l):
    return max(l) - min(l)

print(greatest_diff(numbers))