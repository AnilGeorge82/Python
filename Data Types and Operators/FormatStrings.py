# we cannot combine strings and numbers like this
# age = 38
# txt = "My name is John, I am" + age
# print(txt)

# But we can combine strings and numbers by using the format() method

age = 38
txt = "My name is John, I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 45.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

# using index numbers
quantity = 3
itemno = 567
price = 45.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))
