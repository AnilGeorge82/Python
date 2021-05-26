#lists

num_list = [1, 2.5, 'num', True]
print(num_list)

print(type(num_list))
print(type(num_list[1]))
print(type(num_list[3]))

#lets check the same in a tuple with same values
#Tuples - Ordered elements but immutable, elements cannot be changed once assigned

num_t = (1, 2.5, 'num', True)
print(num_t)
print(type(num_t))
print(type(num_t[2]))

#Dictionary
#is in {} and each record is a key value pair

my_dict =  {"a" : 25,
            "b": 3.4,
            "c" : 20}

print(my_dict)
print(type(my_dict))

#Set
#in {} and an "unordered" collection of "unique" elements

set_a = {5, 2, 3, '1', 4, 4}
print(set_a)
print(type(set_a))