names = ["Sara", "David", "Warner", "Sandy"]
print(names)

new_names = names
print("Original : ", names)
print("Copy : ", new_names)

print(names[1])

new_names[1] = 'Ridley'
print("Original : ", names)
print("Modified : ", new_names)

import copy

companies = ["hackearth", "google", "facebook"]
print(companies)

new_companies = copy.copy(companies)

print("Original : ", companies)
print("Modified : ", new_companies)

new_companies[1] = "microsoft"

print("Original : ", companies)
print("Modified : ", new_companies)

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(old_list)

new_list = copy.copy(old_list)
print("Old list : ", old_list)
print("New list : ", new_list)

print(old_list[1][1])

old_list[1][1] = "Five"
print("Old list : ", old_list)
print("New list : ", new_list)

new_list[2].append("Ten")
print("Original : ", old_list)
print("Modified : ", new_list)

old_list.append([10, 11, 12])
print("Old list : ", old_list)
print("New list : ", new_list)

# copy.copy() created a deep copy of outer list