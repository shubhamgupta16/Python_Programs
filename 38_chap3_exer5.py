# ask a user for name
# Example - Shubham Gupta
# print count of each words
# output : 
#     S : 1
#     h : 2
#     u : 3
#     b : 1
#     a : 2
#     m : 1
#     G : 1
#     p : 1
#     t : 1

# solution:
# name.count("S") , name.count(name[0]) = 1
# name.count("h") , name.count(name[1]) = 2
# name.count("u") , name.count(name[2]) = 1
# name.count("b") , name.count(name[3]) = 1
# name.count("h") , name.count(name[4]) = 2
# name.count("a") , name.count(name[5]) = 1
# name.count("m") , name.count(name[6]) = 1

name = input("please enter your name: ")
i = 0
# name = name.lower()
temp_var = ""
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1