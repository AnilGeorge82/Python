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

number_list = [number for number in range(51) if number % 2 == 0 if number % 5 == 0]
print(number_list)

num = ["Even" if i % 2 == 0 else "Odd" for i in range(30)]
print(num)

numbers = [22, 30, 45, 50, 18, 69, 43, 44, 12]

[x + 1 if x >= 45 else x + 5 for x in numbers]
print(numbers)
z = ["small" if number < 20 else "large" for number in numbers if number % 2 == 0 if number % 3 == 0]
print(z)