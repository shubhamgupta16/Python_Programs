mixed = (1,2,3,4.0)
# looping in tuples

# for loop and tuple
# for i in mixed:
#     print(i)
# Note - You can use while loop too

# tuple with one elements
num = (1,)
words = ('word1',)
# print(type(num))
# print(type(words))

# tuple without parethesis
guitars = 'yamaha', 'baton rouge', 'taylor'
# print(type(guitars))

# tuple unpacking
guitarists = ('Maneli Jamal', 'Eddie Van Der Meer', 'Andrew Foy')
guitarist1, guitarist2, guitarist3 = (guitarists)
# print(guitarist1)

# list inside tuple   [Note: in list you apply all lists functions]
favorites = ('southern magnolia', ['Tokyo Ghoul Theme', 'landscape'])
favorites[1].pop()
favorites[1].append('we made it')
# print(favorites)

# some function that you can use with tuples
# min(), max(), sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))