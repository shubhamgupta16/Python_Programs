# function inside function
# greater(a,b) ---> a or b
# greater(a or b , c) ----> greatest

def greater(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def new_greatest(a,b,c):
    # bigger = greater(a,b)
    return greater(greater(a,b), c)

print(new_greatest(10,20,5))