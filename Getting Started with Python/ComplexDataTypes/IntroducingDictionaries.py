empty_dict = {}
print(empty_dict)
print(type(empty_dict))

bike_owners = {"James" : "Ducati Monster 1200",
                "Jacob" : "Ducati Scrambler 1100",
                "William" : "BMW S 1000 RR",
                "Aiden" : "Harley Davidson"}
print(bike_owners)

print(bike_owners['James'])

int_dict = {1 : 45, 2 : 55, 3 : 65}
print(int_dict)

print(int_dict[2])

#if keys are repeated it considers from the last to first
int_dict = {1 : 45, 2 : 55, 3 : 65, 3 : 75}
print(int_dict)

student_details = {"Henry" : 1995,
                    "Samuel" : 1999,
                    "Ingrid"  : 2005}
print(student_details)

print(student_details.keys())

print("Samuel" in student_details.keys())

print("Andrew" in student_details.keys())

print(student_details.values())

mixed_dict = {False : "Daniel",
                "Aria" : [1, 2, 3],
                "Jacob" : True}
print(mixed_dict)

print(mixed_dict["Aria"])
print(mixed_dict[False])

bike_details = {"bike owner" : "James Smith",
                "bike model" : "Ducati Monster 1200",
                "bike price" : "28140",
                "engine displacement" : "1197"}
print(bike_details)
bike_details['num cylinders'] = 2
print(bike_details)
bike_details['bike price'] = 29140
print(bike_details)
print(bike_details.get('bike price'))

del bike_details["engine displacement"]
print(bike_details)