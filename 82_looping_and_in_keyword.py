# in keyword and iterations in dictionary

user_info = {
    'name' : 'shubham',
    'age' : 23,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}

# check if key exist in dictionary
# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')

# check if value exist in dictionary  ----> values method
# if 23 in user_info.values():
#     print('present')
# else:
#     print('not present')

# loops in dictionaries
# for i in user_info:
#     print(i)

# loops in dictionaries for print values
# for i in user_info.values():
    # print(i)

# values method
user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))
# Note: but these are not lists, you cannot add, delete data from dict values
#       like list, but you can iterate through dict values.
# user_info.values()  ---> return lists
# output: dict_values(['shubham', 23, ['coco', 'kimi no na wa'], ['awakening', 'fairy tale']])

# keys method
user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))
# user_info.keys()  ---> return lists
# output: dict_keys(['name', 'age', 'fav_movies', 'fav_tunes'])

# items method
user_items = user_info.items()
# print(user_items)
# print(type(user_items))
# user_info.items ---> return [(), (), (), ()]
# output: dict_items([('name', 'shubham'), ('age', 23), ('fav_movies', ['coco', 'kimi no na wa']), ('fav_tunes', ['awakening', 'fairy tale'])])

for i, j in user_info.items():
    print(f"key is {i} and value is {j}")