# fromkeys method
# d = {'name' : 'unknown', 'age' : 'unknown'}

# d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
# print(d)

# d = dict.fromkeys(('name', 'age', 'height'), 'unknown')
# print(d)

# d = dict.fromkeys("abc", 'unknown')
# print(d)

# d = dict.fromkeys(range(1,11), 'unknown')
# print(d)

# d = dict.fromkeys(['name', 'age'], ['unknown', 'unknown'])
# print(d)


# get method (useful)
d = {'name' : 'unknown', 'age' : 'unknown'}
print(d['name'])

# when i enter print(d['name']) they give unknown or not present so this type of error is removed by get method
print(d.get('names')) # ---> give 'None' but not through any error 


# Example:
# if 'name' in d:
#     print('present')
# else:
#     print('not present')

# if d.get('name'):
#     print('present')
# else:
#     print('not present')


# clear method ---> to clear dictionary
# d.clear()
# print(d)

# copy method ---> to copy dictionary to another variable
d1 = d.copy()
# d1 = d when you write this so d and d1 point to same dictionary so when change to any one same change happen to both
print(d1)