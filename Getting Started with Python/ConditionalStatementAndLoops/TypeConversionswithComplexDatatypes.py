old_num = '500'
new_num = "10"
remaining_num = int(old_num) - int(new_num)
print(remaining_num)

old_code = '40.6'
new_code = "60.8"
total_code = old_code + new_code
print(total_code)

total_code = float(old_code) + float(new_code)
print(total_code)

my_float = "4.6"
my_int = "6"

total = float(my_float) + int(my_int)
print(total)

value_str = "python world"
value_list = list(value_str)
print(value_list)

print (list((1,2,3,4,5)))

my_tuple = ('Apple', 'Orange', 'Mango', 'Banana')
print(my_tuple)

my_list = list(my_tuple)
print(my_list)

value_str = "python world"
value_tup = tuple(value_str)
print(value_tup)
print('Type of value_str is:', type(value_str))
print('Type of value_tup is:', type(value_tup))

my_list = ['Apple', 'Orange', 'Mango', 'Banana']
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

age_list = [['William', 50], ["Henry", 60], ['James', 90]]
age_tuple = tuple(age_list)
print(age_tuple)

age_tuple = tuple(age_list[0])
print(age_tuple)

pet_list = [('Dog', 1), ('Cat', 2), ('Cow', 3), ('Goat', 4)]
pet_tuple = tuple(pet_list)
print(pet_tuple)

age_tuple = ('Leo', 18,"Aaron", 25, 'Easton', 34)
print(age_tuple)

age_tuple1 = (('Leo', 18) ,("Aaron", 25) , ('Easton', 34))
dict(age_tuple1)
print(age_tuple1)