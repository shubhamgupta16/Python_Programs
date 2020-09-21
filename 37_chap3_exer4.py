# problem
# ask user to input a number containing more than one digit
# example - 1256
# calculate 1+2+5+6 and print


# algorithm - (method to solve problem in human language)
# ask input in string, i.e don't change string to int
# example - "1256"
# pick string character one by one and change to int
# int(example[0]) + int(example[1]) .... go upto len(example)

# user_input = int(input("enter a number containing more than one digit: "))  show error
user_input = input("enter a number containing more than one digit: ")
i = 0
total = 0
# length = len(user_input)
while i < len(user_input):
    total += int(user_input[i])
    i += 1
print(f"sum of {user_input} is {total}") 