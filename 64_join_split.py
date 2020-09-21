# join and split method in list

# split method
# convert string to list
user_info = 'shubham 23'.split()  # or you can pass 'shubham,23'.split(',')
print(user_info)

# join method
# convert list to string
user_info = ['shubham' , '24']  # [Note: here we choose 24 in string because join is work in string]
print(','.join(user_info))