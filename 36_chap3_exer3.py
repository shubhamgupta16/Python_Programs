# exercise one of three
# sum of n natural number
# ask a user for natural number(n)
# print total from 1 to n

n = int(input("enter any natural number: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1

print(f"sum of all natural number up to {n} is {total}")