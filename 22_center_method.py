name = "shubham"

# output - **shubham**
# name.center([string size + how many symbol required to add],"symbol required")
print(name.center(11, "*"))  # add * first right side then left side then so on


# quiz : enter user name then add 4 star left side then 4 star right side
name = input("enter your name : ")
print(name.center(len(name) + 8, "*"))