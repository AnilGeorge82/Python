my_cars_list = ['Tuv 300' , 'Xuv 500', 'Xuv 300', 'Xuv 700', 'Bolero', 'Scorpio']
print(my_cars_list[0:5:])
print(my_cars_list[::2])
print(my_cars_list[0:5:2])
print(my_cars_list[2:5:2])
print(my_cars_list[0:5:3])
print(my_cars_list[1:4:2])
print(my_cars_list[::-1])
print(my_cars_list[2:0:-1])
print(my_cars_list[4:1:-1])
print(my_cars_list[-4:0:-1])
print(my_cars_list[::-2])
print(my_cars_list[::-3])
my_cars_list[6:-1] = ['Ford Focus' , 'Dodge Charger']
print(my_cars_list)
print('Ford Focus' in my_cars_list)
print(my_cars_list.pop(-2))
print('Ford Focus' in my_cars_list)