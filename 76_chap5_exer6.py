# function take a list like [1,2,3, [1,2], [3,4]] , input 
# output: calculate how many lists inside lists
# Hint is use type()

def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

print(sublist_counter([1,2,3,[1,2],[3,4]]))