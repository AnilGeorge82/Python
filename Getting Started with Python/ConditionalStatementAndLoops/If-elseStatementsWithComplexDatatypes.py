fruit_list = ["apple", "orange", "grape", "banana", "avocado"]
if "grape" in fruit_list:
    print("Yes, grape is in the fruit list")
else:
    print("No, grape is not in the fruit list")

if "strawberry" in fruit_list:
    print("strawberry is in fruit list")
elif "orange" in fruit_list:
    print("orange is in the fruit list")
else:
    print("Both strawberry and orange are not in the fruit list")

if fruit_list[1] == "orange":
    print("True")
else:
    print("False")

if fruit_list[4] == "avocado":
    print("Yes, avocado is at the fourth index")
    print("Replacing avocado with strawberry at the fourth index")

    fruit_list[4] = "strawberry"
    print(fruit_list)

else:
    print("avocado is not at the fourth index")

car_tuple = ('Toyota Camry', 'Honda Accord', 'Honda Civic', 'Toyota Corolla')
if "Honda Accord" in car_tuple:
    print("Honda Accord is present in our car tuple")
else:
    print("Honda Accord is not present in our car tuple")

if "Ducati Monster" in car_tuple:
    print("Ducati Monster is present in our car tuple")
else:
    print("Ducati Monster is not present in our car tuple")

if "Ducati Monster" in car_tuple and "Honda Accord" in car_tuple:
    print("Ducati Monster and Honda Accord are both cars")
else:
    print("At least one of Ducati Monster and Honda Accord is not a car")

if "Ducati Monster" in car_tuple or "Honda Accord" in car_tuple:
    print("At least one of Ducati Monster and Honda Accord is not a car")
else:
    print("Neither Ducati Monster nor Honda Accord is a car")

salary_details = {"Lisa": 25000,
                  "Jason": 45000,
                  "Cooper": 35000,
                  "Elias": 23000,
                  "Jordan": 77000}

if "Lisa" in salary_details:
    print("We have salary details for Lisa")
else:
    print("We don't have the salary details for Lisa")

if "Ruby" in salary_details:
    print("We have salary details for Ruby")
else:
    print("We don't have the salary details for Ruby")

if "Cora" in salary_details:
    print("We have salary details for Cora")
else:
    salary_details["Cora"] = 31000
    print("Cora's annual income is %s"%salary_details["Cora"])

age_details = {"Lisa":25, "Jason": 30, "Cooper": 29, "Sarah": 22}

if age_details["Lisa"] < age_details["Jason"]:
    print("Jason is older than Lisa")
    if age_details["Jason"] > age_details["Cooper"]:
        print("Jason is older than Cooper")
        if age_details["Cooper"] < age_details["Sarah"]:
            print("Cooper is younger than Sarah")
        elif age_details["Cooper"] > age_details["Sarah"]:
            print("Jason is the oldest person is the given dictionary")
else:
    print("Jason is not the older person in the given dictionary")

details = [['Jane', 'Amanda', 'Emma'],
           [35, 40, 50],
           [20000, 50000, 40000]]

max_sal = max(details[2])
if(details[2][1] == max_sal):
    if(details[1][1] > 30):
        print(details[0][1], "has the highest salary and her age is greater than 30")

    elif(details[1][1] == 30):
        print(details[0][1], "has the highest salary and she is 30 years old")
    else:
        print("Amanda has the highest salary and her age is less than 30")
else:
    print("Amanda is not the highest paid employee")

