
cars_list = ['Tuv 300' , 'Xuv 500', 'Xuv300', 'Xuv700']
print(cars_list)
cars_list.append('Scorpio')
print(cars_list)

#append method takes only one argument or value and not more than that
#cars_list.append('Bolero', 'Kuv 300')
print(cars_list)
cars_list.insert(5,'Bolero')
print(cars_list)
cars_list.insert(4,'Kuv 5')
print(cars_list)

cars_list.extend(['Marazzo', 'XUV 700'])
print(cars_list)

cars_list2 = ['Hennessey Venom GT', 'Bugatti Veyron', 'Koenigsegg Agera R']
complete_cars_list = cars_list + cars_list2
print(complete_cars_list)

print(complete_cars_list.index('Tuv 300'))
complete_cars_list.remove('Bugatti Veyron')
print(complete_cars_list)

