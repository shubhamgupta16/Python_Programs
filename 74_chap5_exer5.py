# common elements finder function
# define a function which take 2 lists as input and return a list
# which contains common elements of both lists

# example 
# input ---> [1,2,5,8], [1,2,7,6]
# output ---> [1,2]

def common_element(l1,l2):
    output = []
    for i in l1:
        if i in l2 not in output:
            output.append(i)
    return output

print(common_element([1,2,5,8],[1,2,7,6,1,2]))
            