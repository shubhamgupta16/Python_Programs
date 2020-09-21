# list is a data structures
# list ---> this chapter
# ordered collection of items

# you can store anything in lists int, float, string

numbers = [1, 2, 3, 4]
# print whole list
print(numbers)
# print perticular list
print(numbers[1])

words = ["word1", "word2", "word3"]
print(words)
# print word1 and word2 using slicing
print(words[:2])

mixed = [1, 2, 3, 4, "five", "six", 2.3, None]
print(mixed)
# print list last component
print(mixed[-1])
# change second value 2 to "two"
mixed[1] = 'two'
print(mixed)

mixed[1:] = 'two'  
print(mixed)  # output: [1, 't', 'w', 'o']

mixed[1:] = ['three', 'four']
print(mixed)  # output: [1, 'three', 'four']