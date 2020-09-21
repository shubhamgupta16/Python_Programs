# common methods to delete data from list
fruits = ['orange', 'apple', 'pear', 'banana', 'apple', 'kiwi']

# pop method
# fruits.pop() # this remove last element
# fruits.pop(1) # this remove perticular position element
# print(fruits)

# del method    [Note: some people say 'this operator', some people say 'this statement' but this doesn't matter]
# del fruits[1]
# print(fruits)

# remove method  [Note: remove method is used to remove element by name and if you pass element which is not present in list they show you an error]
fruits.remove('orange')
# fruits.remove('mango') # this show you an error because mango is not present in your list
# fruits.remove('apple') # this can remove first position apple element
print(fruits)
