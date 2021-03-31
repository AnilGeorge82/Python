thisdict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
print(thisdict)

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
thisdict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
print(thisdict["brand"])

# Duplicate values will overwrite existing values:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)
print(len(thisdict))

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(thisdict)
