# break and continue keyword

print("**break**")
# break
# try print 1 to 10 but break if go to 5
for i in range(1, 11):
    if i == 5:
        break
    print(i)


print("\n\n")
print("**continue**")
# continue
# print 1 to 10 , but not 5
# 1,2,3,4,6,7,8,9,10
for i in range(1, 11):
    if i == 5:
        continue
    print(i)