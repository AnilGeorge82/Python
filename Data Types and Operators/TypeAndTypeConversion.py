print(type(786))
print(type("786"))
print(type(786.0))
house_number = 25
street_name = "The Crescent"
town_name = "Belmont"
print(type(house_number))
address = str(house_number) + " " + street_name + " , " + town_name
print(address)
grams = "35.0"
print(type(grams))
grams = float(grams)
print(type(grams))
mon_sales = "121"
tues_sales = "200"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales)
print("This week's total sales: " + weekly_sales)