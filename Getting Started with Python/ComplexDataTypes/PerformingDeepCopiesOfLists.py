names = ["Sara", "David", "Warner", "Sandy"]
print(names)

new_names = names.copy()
print("Original : ", names)
print("Modified : ", new_names)
print(new_names[1])
new_names[1] = 'Ridley'
print("Original : ", names)
print("Modified : ", new_names)

#list.copy() function creates a deep copy of a list

import copy

companies = ["hackearth", "google", "facebook"]
print(companies)

new_companies = copy.deepcopy(companies)
print('Original: ', companies)
print('Modified: ', new_companies)
print(new_companies[1])
new_companies[1] = 'microsoft'
print('Original: ', companies)
print('Modified: ', new_companies)

# copy.copy() and copy.deepcopy() produce deep copies of non nested lists

old_list = [[1, 2, 3], [4, 5, 6], [7, 8 ,9]]
print(old_list)

new_list = copy.deepcopy(old_list)
print("Old List: ", old_list)
print("New list: ", new_list)
print(old_list[1][2])
old_list[1][2] = 'Six'
print("Old List: ", old_list)
print("New list: ", new_list)

new_companies = companies[:]
print(new_companies)

new_companies[0] = 'skillsoft'
print('Original: ', companies)
print('Modified: ', new_companies)
