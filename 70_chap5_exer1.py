# define a function which will take list containing numbers as input
# and return list containing square of every elements

# example
# numbers = [1,2,3,4]
# square_list(numbers) ----> return ----> [1,4,9,16]

def square_list(l):
    number = []
    for i in l:
        number.append(i**2)
    return number

number = list(range(1,11))
print(square_list(number))

# which function is not pass in define function  [NOTE: list, str]
