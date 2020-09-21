# dictionaries intro
# Q - why we use dictionaries?
# A - Because of limitations of lists, lists are not enough to represent
#     real data

# Example
user = ['Shubham',24,['coco', 'kimi no na wa'], ['awakening', 'fairy tale']]
# this list contains user name , age , fav movies , fav tunes
# you can do this but this is not a good way to do this.


# Q - what are dictionaries
# A - unordered collections of data in key : value pair.


# how to create dictionaries
user = {'name' : 'Shubham', 'age' : 23}
# print(user)
# print(type(user))

# second method to create dictionary
user1 = dict(name = 'Shubham', age = 23)
# print(user1)


# how to access data from dictionary
# Note - There is no indexing because of unordered collections of data.
# print(user['name'])

# which type of data a dictionary can store?
# Answer: 
#     numbers, string, list, dictionary

user_info = {
    'name' : 'shubham',
    'age' : 23,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}
print(user_info['fav_movies'])


# How to add data to empty dictionary
user_info2 = {}
user_info2['name'] = 'shivam'
user_info2['age'] = 22

print(user_info2)
