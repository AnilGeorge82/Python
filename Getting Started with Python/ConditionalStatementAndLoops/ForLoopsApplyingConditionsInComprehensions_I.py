number_list = [number for number in range(20) if number % 2 == 0]
print(number_list)

multiples_27 = [i for i in range(300) if i % 27 == 0]
print(multiples_27)

string = "Hello 12345 World"
numbers = [int(x) for x in string if x.isdigit()]
print(numbers)

alpha = [x for x in string if x.isalpha()]
print(alpha)

stationery = ["Pen", "Marker", "Ink"]
colors = ["Red", "Blue", "Green"]
combined = [(i, j) for j in stationery for i in colors]
print(combined)