# Sets are mutable and unordered
numbers = [1,2,3,4,4,4,4,5,5,5,6,6,7]
unique_numbers = set(numbers)
print(unique_numbers)
print(len(numbers) - len(unique_numbers))
unique_numbers.add(8)
unique_numbers.pop()
print(unique_numbers)

c = [1,2,2,3,3,4,4,5,5,6,6,6]
d = set(c)
d.add(7)
d.pop()

fruit = {"apple", "banana", "orange", "grapefruit"}
print("watermelon" in fruit)
fruit.add("watermelon")
print(fruit)
print(fruit.pop())
print(fruit)