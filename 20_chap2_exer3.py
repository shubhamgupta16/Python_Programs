# take two comma seprated inputs from user
# 1.) user's name, example - "Shubham"
# 2.) a single character, "h"

# output - 2 print lines
# 1.) user's name length
# 2.) count the character that user inputed (bonus : case insensitive count)

name, alphabet = input("enter your name and single character with comma seprated: ").split(",")
print(f"length of your name is {len(name.strip())}")
# print(f"character count : {name.lower().count(alphabet.lower())}")

# solve problem using strip method
print(f"character count : {name.strip().lower().count(alphabet.strip().lower())}")