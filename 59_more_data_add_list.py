# More method to add data

# some more methods to add data in our list
# insert method
# how to join(concatenate) two list
# extend method
# difference between append and extend method

fruits1 = ['mango', 'orange']

# insert data to perticular position using insert position
# fruits1.insert(1, "grapes")
# print(fruits1)

fruits2 = ['grapes', 'apple']

# fruits = fruits1 + fruits2
# print(fruits)

# without using third variable using extend method
fruits1.extend(fruits2)
print(fruits1)  # output: ['mango', 'orange', 'grapes', 'apple']
print(fruits2)  # output: ['grapes', 'apple']

# if i use append method agains extend methos
fruits1.append(fruits2)
print(fruits1) # output: ['mango', 'orange', 'grapes', 'apple', ['grapes', 'apple']]