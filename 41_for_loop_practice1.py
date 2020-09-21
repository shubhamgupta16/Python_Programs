# practice for Loop
# ask user a number like 1256
# calculate sum of digits ---> 1 + 2 + 5 + 6

total = 0
num = input("enter a number: ")
for i in range(len(num)):
    total += int(num[i])

print(total)