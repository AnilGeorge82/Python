thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#Get Keys

x = thisdict.keys()
print(x)

#Add a new item to the original dictionary, and see that the keys list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x)

car["color"] = "white"

print(x)

#Make a change in the original dictionary, and see that the values list gets updated as well

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x)

car["year"] = 2020

print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x)

car["color"] = "red"

print(x)

# The items() method will return each item in a dictionary, as tuples in a list.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x)

car["year"] = 2020

print(x)

#Check if Key Exists
#To determine if a specified key is present in a dictionary use the in keyword

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in thisdict dictionary")

