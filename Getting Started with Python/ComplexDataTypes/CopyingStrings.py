old_str = "Python"
print(old_str)

new_str = old_str
print(old_str)
print(new_str)
print(new_str[2])

import copy

first_str = 'Will'
print(first_str)

second_str = copy.copy(first_str)
print("First String: ", first_str)
print("Second String: ", second_str)

second_str = 'Smith'

print("First String: ", first_str)
print("Second String: ", second_str)

first_str = 'Johnny'
print(first_str)

second_str = copy.deepcopy(first_str)

print("First String: ", first_str)
print("Second String: ", second_str)

second_str = 'Depp'

print("First String: ", first_str)
print("Second String: ", second_str)
