# something more about tuples, list, str

nums = tuple(range(1,11))
print(nums)

# tuple converted to list
nums = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(nums)

# tuple convert to string
nums = str((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# output: "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"
print(nums)
print(type(nums))

# list convert to string
nums = str([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(nums))