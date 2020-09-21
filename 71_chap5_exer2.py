# define a function which will take list as a argument and this function
# will return a reversed list

# examples
# [1,2,3,4] ---> [4,3,2,1]
# ['word1', 'word2'] ---> ['word2', 'word1']

# Note you simply do this with reverse method or [::-1]

# but try to do this with the help of append and return method

# def reversed_list(l):
#     reversed = []
#     for i in l[::-1]:
#         reversed.append(i)
#     return reversed

# or 
# def reversed_list(l):
#     return l[::-1]

# another method
# def reversed_list(l):
#     l.reverse()
#     return l 

# by pop method
def reversed_list(l):
    r_list = []
    for i in range(1, len(l)+1):
        pop_item = l.pop()
        r_list.append(pop_item)
    return r_list

number = list(range(1,11))
print(reversed_list(number))