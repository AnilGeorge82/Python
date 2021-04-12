cars = ["Ford", "Volvo", "BMW"]
print(cars)


car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

#Get the value of the first array item:
x = cars[0]
print(x)

#Modify the value of the first array item:
cars[0] = "Toyota"
print(cars)

#Return the number of elements in the cars array:
x = len(cars)
print(x)

#You can use the for in loop to loop through all the elements of an array.
for x in cars:
    print(x)

#You can use the append() method to add an element to an array.

cars.append("Honda")
print(cars)

#You can use the pop() method to remove an element from the array.

cars.pop(1)
print(cars)

#Delete the element that has the value "BMW":

cars.remove("BMW")
print(cars)