# EXERCISE - WATCH COCO
# Ask user's name and age
# If user's name start with ('a' or 'A') and age is above 10 then
# Print 'you can watch coco movei'
# Else print 'sorry, you cannot watch coco'

user_name = input("enter your name: ")
user_age = int(input("enter your age: "))
# if user_age >= 10 and (user_name[0] == 'a' or user_name[0] == 'A'):
if user_name[0].lower() == 'a' and user_age >= 10:
    print("you can watch coco movei")
else: 
    print("sorry, you cannot watch coco")