# practice for loop
# ask user name and count each character
# "Shubham Gupta"
# S : 1
# h : 2
# u : 2
# b : 1
# a : 2
# m : 1
#   : 1
# G : 1
# p : 1
# t : 1

name = input("enter your name : ")
temp = ""
for i in range(0, len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]