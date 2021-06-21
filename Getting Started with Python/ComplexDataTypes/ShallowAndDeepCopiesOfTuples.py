# Tuples - Shallow and Deep copies
fruits = ("apple", "banana", "cherry")
print(fruits)

new_fruits = fruits
print("Original: ", fruits)
print("Modified: ", new_fruits)

print(new_fruits[2])

#new_fruits = fruits Both variables refer to the same tuple in memory - item assignment not supported as they are immutable

fruits = ("apple", ["banana", "cherry"], "blackcurrant")
print(fruits)

new_fruits = fruits
print("Original: ", fruits)
print("Modified: ", new_fruits)

print(new_fruits[1][0])

new_fruits[1][0] = 'orange'
print("Original: ", fruits)
print("Modified: ", new_fruits)

# assignment in the list within the tuple created a shallow list affecting both the original and modified tuples

import copy

bikes = ('Honda', 'Suzuki', 'Triumph', ['Kawasaki', 'Ducati'])
print(bikes)

new_bikes = copy.copy(bikes)
print("Original: ", bikes)
print("Modified: ", new_bikes)
print(new_bikes[3][0])

new_bikes[3][0] = 'Dodge'
print("Original: ", bikes)
print("Modified: ", new_bikes)

new_bikes = copy.deepcopy(bikes)
print("Original: ", bikes)
print("Modified: ", new_bikes)

new_bikes[3][0] = 'Harley Davidson'
print("Original: ", bikes)
print("Modified: ", new_bikes)

#copy.deepcopy sucessfully allows changes in the copied tuple containing a nested list,changes are allowed only to the elements of that nested list
