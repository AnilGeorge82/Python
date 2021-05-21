my_tuple= ()
print(my_tuple)
print(type(my_tuple))
int_tuple = (1,2,3)
print(int_tuple)
str_tuple = ("Hello" , "Python")
print(str_tuple)

print(int_tuple , str_tuple)

combined_tuple = int_tuple + str_tuple
print(combined_tuple)

print(str_tuple * 3)

mixed_tuple = (1, "Hello", 3.4)
print(mixed_tuple)

my_tuple = 1, "Hello", 3.4
print(my_tuple)

a,b,c = my_tuple
print(a)
print(b)
print(c)

nested_tuple = (1,2,3,(4,5,6))
print(nested_tuple)

mixed_tuple = ("mouse", [8,4,6],(1,2,3))
print(mixed_tuple)

my_tuple = ('p','e','r','m','i','t')
print(my_tuple)
print(my_tuple[0])
print(my_tuple[5])

print(mixed_tuple[1])
print(mixed_tuple[1][0])
print(mixed_tuple[2][2])

my_tuple = ('E', 'l', 'e', 'p', 'h', 'a', 'n', 't')
print(my_tuple[1:])
print(my_tuple[2:4])
print(my_tuple[::2])
print(my_tuple.index('l'))
print('e' in my_tuple)
print('b' in my_tuple)
print('b' not in my_tuple)
int_tuple = (1, 4, 9, 9)
print(sum(int_tuple))
print(list(int_tuple))
print(set(int_tuple))