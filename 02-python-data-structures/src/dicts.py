my_dict = {
    'name':'joe',
    'age':28
}

# Add a key/value pair
my_dict['name']

# Update a value
my_dict["phone"] = 555-555-5555

# Use an invalid key
my_dict['badkey'] #raises KeyError

# Test if a key exists
"name" in my_dict

# use .get()
my_dict.get("name", 'default value: missing value')

# Delete a key
my_dict.pop('name')
del my_dict['age']

# get the length of a dict
len(my_dict)

# Merge two dicts
x = {'age': 12, 'phone': 123-345-3544}
my_dict.update(x)

# copy a dict
my_dict.copy().update()

# loop over a dict
for key in my_dict:
    print(key, my_dict[key])
    
for key in my_dict.items():
    print(key, value)