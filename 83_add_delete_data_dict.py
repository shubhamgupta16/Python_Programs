# add and delete data
user_info = {
    'name' : 'shubham',
    'age' : 23,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}

# how to add data
# user_info['fav_songs'] = ['song1', 'song2']
# print(user_info)


# pop method
# user_info.pop() ---> if pop() is empty so through an error
# popped_item = user_info.pop('fav_tunes')
# print(f"popped item is {popped_item}")
# print(user_info)
# print(type(popped_item ))  # ---> return list because data in list


# popitem method
# note: when you require to delete any one random 'key and value pair' so use popitem method
popped_item = user_info.popitem()
print(user_info)
print(popped_item)
print(type(popped_item))  #---> return tuple
