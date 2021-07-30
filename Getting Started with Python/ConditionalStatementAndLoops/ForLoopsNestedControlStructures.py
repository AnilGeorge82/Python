us_cities = ["New York", "Nashville", "Seattle"]
for city in us_cities:
    if city == "New York":
        print("New York is present in the list")

numbers = [11, 33, 55, 39, 2, 55, 75, 37, 22, 23, 42, 13, 4294967296]

for num in numbers:
    if num % 2 == 0:
        print("The list contains an even number:", num)
        
years = [2016, 2017, 2018, 2019, 2020]

for year in years:
    if year % 4 == 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

names = [["Mary", "Linda", "Jessica"], ["James", "Jacob", "William"]]

for sublist in names:
    print(sublist)

for sublist in names:
    for name in sublist:
        print(name)

colors_list = ["Red", "Green", "Blue"]
objects_list = ["Pen", "Marker", "Pencil"]

for color in colors_list:
    for obj in objects_list:
        print(color, obj)
