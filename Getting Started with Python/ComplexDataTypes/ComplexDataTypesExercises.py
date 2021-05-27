# Similarities between Lists and Tuples

# Ordered collection of elements
# Ordering is preserved and is significant
# Can contain elements of different data types
# Elements are accessed using index values starting from 0
# Slicing operations can be performed on both

# Differences between Lists and Tuples
# Tuples are immutable, Lists are mutable
# Tuples once created cannot be edited

new_list = ['Amy', 'Bob', 'Charlie', 'Daisy']
print(new_list[0])
print(new_list[3])

print(new_list[0:1])

print(new_list[0:3])

print(new_list[1:4])

new_tuple = ('Amy', 'Bob', 'Charlie', 'Daisy')

print(new_tuple[1])

print(new_tuple[0:3])

print(new_tuple[1:3])
