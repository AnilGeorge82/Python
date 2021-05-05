a = 10
a += 1
print(a)


cars_list = ['Tuv 300', 'Xuv 500', 'Xuv300', 'Xuv700']
print(cars_list)
cars_list.append('Scorpio')
print(cars_list)

# append method takes only one argument or value and not more than that
#cars_list.append('Bolero', 'Kuv 300')
print(cars_list)
cars_list.insert(5, 'Bolero')
print(cars_list)
cars_list.insert(4, 'Kuv 5')
print(cars_list)

cars_list.extend(['Marazzo', 'XUV 700'])
print(cars_list)

cars_list2 = ['Hennessey Venom GT', 'Bugatti Veyron', 'Koenigsegg Agera R']
complete_cars_list = cars_list + cars_list2
print(complete_cars_list)
complete_cars_list.sort()
print(complete_cars_list)

complete_cars_list.reverse()
print(complete_cars_list)

complete_cars_list.pop()
print(complete_cars_list)

complete_cars_list.append('Tuv 300')
print(complete_cars_list)

print(complete_cars_list.count('Tuv 300'))
print(set(complete_cars_list))

print(cars_list.clear())

# Deep copy
new_cars_list = complete_cars_list.copy()
print(new_cars_list)

del complete_cars_list

print(new_cars_list)

# shallow copy = all changes that are done on one will have the same impact on the copy

another_cars_list = new_cars_list
print(another_cars_list)

another_cars_list.remove('Hennessey Venom GT')
print(another_cars_list)

new_cars_list.remove('Xuv300')
print(new_cars_list)
print(another_cars_list)
