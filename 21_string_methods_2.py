# replace() method
# find() method

string = "she is beautiful and she is good dancer"
print(string.replace(" ", "_"))

print(string.replace("is", "was", 1)) # in this replace 'is' by 'was' only first so if required to replace also second 'is' so 1 change to 2


print(string.find("is"))

# if find second 'is'
is_pos1 = string.find("is") # is_pos1 ---> number
is_pos2 = string.find("is" , is_pos1 + 1)
print(is_pos2)