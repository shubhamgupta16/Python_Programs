user_info = {
    'name' : 'shubham',
    'age' : 23,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}

more_info = {'name': 'Shubham Gupta','state' : 'Uttar Pradesh', 'hobbies' : ['coding','reading','cricket']}


user_info.update(more_info)
# user_info.update({}) #if i pass {} in update method nothing happen only method run

print(user_info)