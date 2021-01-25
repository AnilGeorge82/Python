#Dictionary - a data type for MUTABLE objects that store mappings of unique keys to values

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
print(elements['carbon'])
elements['lithium'] = 3
print(elements)
print('mithril' in elements)
print(elements.get('dilithium'))
print(elements.get('lithium'))
x = elements.get('dilithium')
is_null = x is None
print(is_null)

population = {'Shanghai' : 17.8,
'Istanbul' : 13.3,
'Karachi' : 13.0,
'Mumbai' : 12.5}
print(population)