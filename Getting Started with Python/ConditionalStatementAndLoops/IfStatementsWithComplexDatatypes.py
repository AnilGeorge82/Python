tuple_teachers = ("Alice", "Alexa", "Robert", "Bella")
print(tuple_teachers)

if "Alexa" in tuple_teachers:
    print("Alexa is a teacher")

student_score = {"Ayden":60, "Gavin" : 85, "Ian" : 76, "Jose": 70, "Jane" :82}
print(type(student_score))

if "Ian" in student_score:
    print("Ian is in the student_score dictionary")

if "Jane" in student_score:
    print("Jane's score: ", student_score["Jane"])

if "Ayden" in student_score:
    print("Ayden's score: ", student_score["Ayden"])

a = 60
b = 35

if a>b and b<a:
    print("a is greater than b")

if a>b and b>a:
    print("a is greater than b")

x_value = 65
y_value = 25
print(x_value)
print(y_value)

z_value = x_value + y_value
print(z_value)

if x_value > y_value and y_value < z_value:
    print("Both conditions are True")

if a > b or b < a:
    print("At least one of the above conditions is true")

bike_price = 716

bike_is_electric = False

if bike_price > 500 or bike_is_electric:
    print("At least one of the above conditions is true")

if bike_price > 1000 or bike_is_electric:
    print("At least one of the above conditions is true")

if not bike_is_electric:
    print("It's a human-powered bike")
    
x = 45
y = 78

if not (x < y):
    print("x is not less than y")

if not (x > y):
    print("x is not less than y")


