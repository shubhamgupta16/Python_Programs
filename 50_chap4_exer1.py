# define a function which takes two numbers as a input and 
# return greater of two numbers.

def greater(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
print(f"Greater number is : {greater(num1, num2)}")