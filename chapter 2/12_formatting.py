name = "Shubham"
age = 23
print("hello " + name + " your age is " + str(age)) # ugly syntax

# String Formatting 
# python 2
# python 3
# python 3.6 (best)


# python 3
print("hello {} your age is {} ".format(name, age))

# python 3.6
print(f"hello {name} your age is {age}")

# if required to increase age by 2
# print("hello {} your age is {} ".format(name, age + 2))
# print(f"hello {name} your age is {age + 2}")