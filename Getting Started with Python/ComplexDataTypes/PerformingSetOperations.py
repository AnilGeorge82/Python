number1 = {1, 2, 3, 4, 5}
number2 = {4, 5, 6, 7, 8}
number3 = {7, 8, 9, 10, 11}

#unifying sets - duplicates are eliminated 
print(number1.union(number2))

number_union = number1.union(number2, number3)
print(number_union)

student_set_1 = {"Ava", "Emma", "James"}
student_set_2 = {"James", "Mia", "Olivia"}
student_set_3 = {"Olivia", "Sarah", "Sofia"}
print(student_set_1.union(student_set_2, student_set_3))

print(number1)

print(number2)

print(number3)

# Intersection finds out the common elements

print(number2.intersection(number1))

# difference will bring in the balance or the difference

print(number1.difference(number2))

diff_set = student_set_1.difference(student_set_2)
print(diff_set)

number1.intersection_update(number2)
print(number1)


student_set_1.difference_update(student_set_2)
print(student_set_1)

student_set_1.intersection_update(student_set_2)
print(student_set_1)

print({1, 2, 3}.isdisjoint({4, 5, 6}))


print({1, 2, 3}.isdisjoint({1, 5, 6}))

print({10, 20}.issubset({10, 20, 30}))

print({10, 20, 30}.issuperset({10, 20}))