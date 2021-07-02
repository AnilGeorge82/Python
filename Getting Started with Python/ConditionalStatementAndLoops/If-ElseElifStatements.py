if 10 > 20:
    print("10 is greater than 20")
    print("if block activated")
else:
    print("10 is less than 20")
    print("else block activated")

bike_price = 7160
if bike_price <= 8000:
    print("It's a cheap bike")
    print("if block activated")
else:
    print("It's an expensive bike")
    print("else block activated")

bike_price = 9000
if bike_price <= 8000:
    print("It's a cheap bike")
    
else:
    print("It's an expensive bike")

# Ternary operators (conditional expressions) evaluate something based on a condition being true or not

num = 50
print("num before expression: ", num)
num = num - 20 if num > 20 else num +20
print("num after expression: ", num)

num = 50
print("num before expression: ", num)
if num > 20:
    num = num - 20  
else: 
    num = num + 20
print("num after expression: ", num)

num = 100
print("Number before expression: ", num)
result = num / 5 if num < 50 else num * 5
print("num after expression: ", result)

if 15 > 20:
    print("15 is greater than 20")
    print("if block activated")

elif 15 < 20:
    print("15 is less than 20")
    print("elif block activated")
else:
    print("Both are equal")
    print("else block activated")

#elif is used to chain together if-else conditions. The conditions are evaluated in order

a = 45
b = 45

if b > a:
    print("b is greater than a")
    print("if block activated")

elif a == b:
    print("a and b are equal")
    print("elif block activated")
else:
    print("a is greater than b")
    print("else block activated")
