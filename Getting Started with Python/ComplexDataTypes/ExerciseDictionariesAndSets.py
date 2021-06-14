# Dictionaries in Python
# Unordered collection of Key Value Pairs
# Every key is associated with a value
# Each key in a dictionary is unique, values can be duplicates
# Values are looked up by key
# Dictionaries are mutable, keys can be added, values can be updated
bike_owners = {"James" : "Ducati Monster 1200",
                "Jacob" : "Ducati Scrambler 1100",
                "William" : "BMW S 1000 RR",
                "Aiden" : "Harley Davidson"}
print(bike_owners)
print(bike_owners['Jacob'])

# Sets in Python
# Unordered collection of unique elements
# Adding duplicates to sets will add the element exactly once
# Cannot contain mutable elements 1.e, Lists or dictionaries within sets
# Can perform set operations such as union, intersection, difference etc.
set_string = {"Emma", "Olivia", "Ava", "Mia"}
print(set_string)

# Comparing Lists, Dictionaries and Sets
# Lists are ordered collections, both dictionaries and sets are unordered
# List can contain duplicates, sets cannot contain duplicates, dictionaries cannot have duplicate keys
# Lists can contain nested complex data types and so can values in dictionaries
# Sets can contain only immutable tuples and cannot contain other complex data types
# List elements can be looked up by index
# No lookup for set elements
# Dictionary values can be looked up by key
