set_string = {"Emma", "Olivia", "Ava", "Mia"}
print(set_string)

empty_set = set()
print(empty_set)

print(type(empty_set))

mixed_set = {"Emma", 5, 1.5, True}
print(mixed_set)

mixed_set1 = {"Emma", 5, 1.5, True, (1,2,3)}
print(mixed_set1)

#Sets can only contain Immutable elements - it cannot have a list or a dictionary within it which is mutable

#set_list = {1, 2, 3, [4, 5, 6]}

#print(set_list)

set_tuple = {1, 2, 3, (4, 5, 6)}
print(set_tuple)

# duplicates are eliminated from a set
student_set = {"Emma", "Olivia", "Ava", "Mia", "Emma", "Ava"}
print(student_set)

set_int = {1, 3, 4, 5, 6, 2, 5, 3, 4}
print(set_int)

set_1 = {1, 3, 4, 8, 'a', 6, 2, 10, 3, 4}
print(set_1)

set_1.add(9)
print(set_1)

set_1.add(9.5)
print(set_1)

set_1.add(9)
print(set_1)

teachers_set = {"Emma", "Olivia", "Ava", "Mia", "Avery", "Jacob", "Daniel"}
print(teachers_set)

print(len(teachers_set))

print(max(teachers_set))

print(min(teachers_set))

teachers_set.discard('Emma')
print(teachers_set)

teachers_set.remove('Mia')
print(teachers_set)

teachers_set.clear
print(teachers_set)