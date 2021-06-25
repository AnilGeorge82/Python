set_1 = {'c++', 'php', 'java', 'python'}
print(set_1)

set_2 = set_1   
print("Original: ", set_1)
print("Modified: ", set_2)

set_2.add('sql')
print("Original: ", set_1)
print("Modified: ", set_2)

print(set_2.pop())
print("Original: ", set_1)
print("Modified: ", set_2)

# Sets can contain only immutable data structures such as Tuples and not lists

set_1 = {'c++', 'php',('java', 'python'), 'sql'}
set_2 = set_1
print("Original: ", set_1)
print("Modified: ", set_2)

import copy

teachers_set = {"Ava", "Mia", "Jacob", "Daniel"}
print(teachers_set)

new_teachers_set = copy.copy(teachers_set)
print(teachers_set)
print(new_teachers_set)

teachers_set.add("Emma")
print(teachers_set)
print(new_teachers_set)

new_teachers_set.remove("Ava")
print(teachers_set)
print(new_teachers_set)

teachers_set = {"Ava", "Mia", "Jacob", "Daniel"}

new_teachers_set = copy.deepcopy(teachers_set)
print(teachers_set)
print(new_teachers_set)

teachers_set.add("Emma")
print(teachers_set)
print(new_teachers_set)

teachers_set.remove("Emma")
print(teachers_set)
print(new_teachers_set)
