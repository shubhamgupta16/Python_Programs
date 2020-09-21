# find greatest number between three number
def greatest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
print(f"greatest number is {greatest(num1, num2, num3)}")