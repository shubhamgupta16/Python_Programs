name = "     Shubham     "
dots = "..............."

print(name + dots)

# lstrip() method
print(name.lstrip() + dots)

# rstrip() method
print(name.rstrip() + dots)

# strip() method
print(name.strip() + dots)

# if in your string have middle space like name = "Shu    bham"
name = "Shu    bham"
print(name.replace(" ", "") + dots)
