#Ask user to input 3 numbers and you have to print average of three numbers using string formatting.

#Bonus :- try to take all three comma separated inputs in one line.

# find average of three numbers
number1, number2, number3 = input("Enter three numbers seprated by comma: ").split(",") 
print(f"Average of {number1}, {number2} and {number3} is {(int(number1) + int(number2) + int(number3))/3}")