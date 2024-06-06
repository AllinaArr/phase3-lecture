my_list = ["a", 'b', 'c', 'd', 'e', 'f', 'g']

for item in my_list:
    print(item)
    
for i in range(0, len(my_list)):
    print(i, my_list[i])
    
#map
my_list = [1,2,3,4]

def double(numbers):
    "Double every number in numbers"
    
    new_list = [] #create empty list
    for num in numbers: #loop over every number
        new_num = num * 2 #transforming the number
        new_list.append(new_num) #add to new_list
    return new_list

print(my_list)
print(double(my_list))


#filter
my_list = [1,2,3,4,5,6]

def get_posis(numbers):
    "Returns a new list with negative numbers filtered out"
    
    new_list = [] #create empty list
    for num in numbers: #loop over existing list
        if num > 0: #check condition
            new_list.append(num) #add to new_list
    return new_list

print(my_list)
print(get_posis(my_list))
