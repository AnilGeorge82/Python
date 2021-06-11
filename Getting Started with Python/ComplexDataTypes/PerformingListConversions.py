my_list = ['Leo', 18,
            'Aaron', 25,
            'Easton', 34,
            'Jordan', 30]
print(my_list)
tuple(my_list)
print(my_list)

my_list1 = [['Leo', 18,
            'Aaron', 25,
            'Easton', 34,
            'Jordan', 30]]

print(my_list1)

print(tuple(my_list1))

students_list = [[1, 'Caleb', 2, 'Leo'], [3, 'Easton', 4, 'Jordan']]
print(students_list)


students_list2 = [[1, 'Caleb'], [2, 'Leo'], [3, 'Easton'], [4, 'Jordan']]
print(students_list2)
print(dict(students_list2))

students_list3 = [[1, 'Caleb'], [2, 'Leo'], [3, 'Easton'], [4, 'Jordan', 'Adam']]
students_list4 = [[1, 'Caleb'], [2, 'Leo'], [3, 'Easton'], [4, ['Jordan', 'Adam']]]
print(dict(students_list4))

car_matrix = [['Hennessey Venom GT', 1244],
              ['SSC Ultimate Aero', 1287],
              ['Zenvo STI', 1100]]
car_matrix_dict = dict(car_matrix)
print(car_matrix)
car_matrix.pop()
print(car_matrix)
car_matrix.clear
print(car_matrix_dict)
car_names = list(car_matrix_dict)
print(car_names)
car_hp = list(car_matrix_dict.values())
print(car_hp)