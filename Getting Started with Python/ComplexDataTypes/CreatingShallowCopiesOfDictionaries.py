months = {'jan': 1, 'feb': 2, 'march': 3, 'april': 4}
print(months)

new_months = months
print("Original: ", months)
print("Modified: ", new_months)

print(new_months['feb'])

new_months['feb'] = 'FEB'
print("Original: ", months)
print("Modified: ", new_months)

import copy

employees = {"Alison" : 2007, "Bart" : 2008, "Cathy" : 2009, "Dan" : 2010}
print(employees)

employees_copy = copy.copy(employees)
print(employees)
print(employees_copy)

print(employees["Alison"])

employees_copy["Alison"] = 2005
print(employees)
print(employees_copy)

orig_dict = {'one' :1, 'two':2, 'three':3, 'four':[1,2,3,4.0]}
print(orig_dict)

new_dict = copy.copy(orig_dict)
print("Original: ", orig_dict)
print("Modified: ",new_dict)

new_dict['four'][3] = 'FOUR'
print("Original: ", orig_dict)
print("Modified: ",new_dict)

#copy.copy(dict) produces a deep copy of the outer dictionary but a shallow copy of nested types

new_dict['four'].append(5)
print("Original: ", orig_dict)
print("Modified: ",new_dict)

orig_dict = {'one':1, 'two':2, 'three': {'zero':0, 'one': 1}, 'four':4}
print(orig_dict)

new_dict = copy.copy(orig_dict)
print(orig_dict)
print(new_dict)

new_dict['three']['zero'] = 'ZERO'
print(orig_dict)
print(new_dict)
