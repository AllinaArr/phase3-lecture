my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Test if an element exists in `my_list`
"a" in my_list

# Add element to the end
my_list.append("h")

# Insert element at an index
my_list.insert(0, "x")

# Merge two lists together
[1,2] + [3,4]

# Duplicate a list
my_list.copy()

# Index lookup
my_list[0]
my_list[2]
my_list[-5]

# Slice
my_list[0:3]

# Get length
len(my_list)

# Get min/max
min(my_list)
max(my_list)

# Find index of an element
my_list.index("b")

# Count number of instances of an element
my_list.count("b")

# Remove element from list
# deletes the last element in the list
my_list.pop() 
# we can add an index
my_list.pop(2)


# Sorting (with an without a key)
my_list.sort()
my_list.sort(reverse=True)

# sorted() vs .sort()
sorted(my_list)
sorted(my_list, reverse=True)
