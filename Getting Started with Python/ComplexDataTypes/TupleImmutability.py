immutable_tuple_1 = (0, 1, 2, 3)
print(immutable_tuple_1)

#immutable_tuple_1 [0] = 4
#print(immutable_tuple_1)
#will result in TypeError: 'tuple' object does not support item assignment

immutable_tuple_2 = (4,2,3,[6,5])
print(immutable_tuple_2)
print(immutable_tuple_2[0])
print(immutable_tuple_2[3])

immutable_tuple_2[3][1] = 100
print(immutable_tuple_2)

my_tuple = ('p' , 'y', 't', 'h', 'o', 'n')
#del my_tuple[3]
#print(my_tuple)
#TypeError: 'tuple' object doesn't support item deletion
#del my_tuple
#print(my_tuple)

tuple_a = (1, 2, 3, 4, 5)
tuple_b = ('a' , 'b' , 'c' , 'd' , 'e')

zipped = zip(tuple_a, tuple_b)
print(zipped)

result = tuple(zipped)
print(result)

tuple_x, tuple_y = zip(*result)

print('tuple_x :', tuple_x)
print('tuple_y :', tuple_y)

list_a = [6, 7, 8, 9, 10]
list_b = ['a', 'e', 'i', 'o', 'u']
zipped_list = zip(list_a, list_b)
result = list(zipped_list)
print(result)

a = ("John", "Charles", "Mike")
b = ("Manager", "Supervisor", "Engineer")
x = zip(a,b)
print(x)
result = tuple(x)
print(result)

a = ("John", "Charles", "Mike")
b = ("Manager", "Supervisor", "Engineer")
y = zip(a,b)
print(dict(y))

numbers_list = [1, 2, 3]
str_list = ['one', 'two', 'three']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')
result = zip(numbers_list, numbers_tuple)
print(result)
result_set = set(result)
print(result_set)

result = zip(numbers_list, str_list, numbers_tuple)
result_set = set(result)
print(result_set)