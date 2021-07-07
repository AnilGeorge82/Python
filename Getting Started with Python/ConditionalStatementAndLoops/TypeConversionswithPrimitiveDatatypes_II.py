print(type(66))
print(float(66))
a = 66
print(type(a))

my_float = float(a)
print(my_float)
print(type(390.8))

print(int(390.8))

b = 66.7
my_int = int(b)
print(my_int)

num_int = 76
num_float = 23.45

print("datatype of num_int:", type(num_int))
print("datatype of num_float:", type(num_float))

new_num = num_int + num_float
print(new_num)
print("datatype of new_num is", type(new_num))

my_float = 66.999999

my_num = int(my_float)
print(my_num)

a = 125.0
b = 390.8

print(int(a))
print(int(b))

print(int('12'))

a ='66'
print(type(a))

my_int = int(a)
print(my_int)

print(type(my_int))

num_int = 123
num_str = "456"

print("data type of num_int:", type(num_int))
print("data type of num_str:", type(num_str))

num_str = int(num_str)
print("data type of num_str:", type(num_str))

sum_value = num_str + num_int
print(sum_value)
print("data type of sum_value:", type(sum_value))

#integers can be expressed in different base formats - hexadecimal: base 16, binary: base 2, octal: base 8

my_float = 5524.53
print("John has " + str(my_float) + " points.")

user = "John"
lines = 50

print("Congratulations, " + user + "! You just wrote " + str(lines) + " lines of code.")

number = 15
plus_ten = number + 10
plus_twenty = number + 20
print("\nIf we add 10 and 20 to this number, we get %s and %s" %(plus_ten, plus_twenty))