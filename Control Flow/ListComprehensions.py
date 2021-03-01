cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

print(capitalized_cities)

squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
first_names = [name.split()[0].lower() for name in names]
print(first_names)

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
first_names = [name.split()[0].upper() for name in names]
print(first_names)

multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)