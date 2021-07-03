bike_price = 20000

if bike_price < 6000:
    print("It's a cheap bike")
elif bike_price >= 6000 and bike_price < 10000:
    print("It's a moderately price bike")
elif bike_price >= 10000 and bike_price < 15000:
    print("It's a somewhat expensive bike")
elif bike_price > 6000:
    print("It's a very expensive bike")

# Nested If statement
x = 25
y = 35
z = 45

if x < y:
    print("The first condition is true")
    if x < z:
        print("Both conditions are true")
    else:
        print("The first condition is true, the second one is false")

x = 55

if x < y:
    print("The first condition is true")
    if x < z:
        print("Both conditions are true")
    else:
        print("The first condition is true, the second one is false")
else:
    print("The first condition is false")

#age = int(input("Enter your age: "))

age = 21
if age >= 15:
    if age > 20:
        print("You are too old for this camping trip!")
    else:
        print("You are of the right age for this camping trip!")

else:
    print("You are too young for this camping trip!")
