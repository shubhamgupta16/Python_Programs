# filter odd even
# define a function
# input
# list ---> [1,2,3,4,5,6,7]
# output ---> [[1,3,5,7],[2,4,6]]

def seprate_element(l):
    even = []
    odd = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    output = [odd,even]
    return output

number = list(range(1,8))
print(seprate_element(number))