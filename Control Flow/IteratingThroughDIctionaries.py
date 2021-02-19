# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

fruit_count, not_fruit_count = 0, 0

basket_items = {'apples': 4, 'oranges': 56, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for object, count in basket_items.items():
    if object in fruits:
        fruit_count += count
    else:
        not_fruit_count += count
print("The number of fruits is {}. There are {} objects that are not fruits".format(fruit_count, not_fruit_count))

toycar_count, not_toycar_count = 0, 0

basket_items = {'monster truck': 45, 'oranges': 12, 'hotwheels': 56, 'bananas': 34}
toycar = ['monster truck', 'hotwheels']

for object, count in basket_items.items():
    if object in toycar:
        toycar_count += count
    else:
        not_toycar_count += count
    print("The number of toy cars is {}. There are {} objects that are not toy cars.".format(toycar_count, not_toycar_count))
    
#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items():
    if object in fruits:
        result += count
        
print("There are {} fruits in the basket.".format(result))

print(result)

#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items():
    if object in fruits:
        result += count
        
print("There are {} fruits in the basket.".format(result))

print(result)


#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items():
    if object in fruits:
        result += count
        
print("There are {} fruits in the basket.".format(result))

print(result)

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

for object, count in basket_items.items():
  if object in fruits:
        fruit_count += count
  else:
        not_fruit_count += count
        
print("The number of fruits is {}. There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))

