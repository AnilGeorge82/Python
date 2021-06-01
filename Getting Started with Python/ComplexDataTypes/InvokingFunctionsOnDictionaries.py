bike_details = {"bike owner" : "James Smith",
                "bike model" : "Ducati Monster 1200",
                "bike price" : "28140",
                "engine displacement" : "1197"}
print(bike_details)

print(len(bike_details))
print(len(bike_details.keys()))
print(len(bike_details.values()))
print(sorted(bike_details))
print(sorted(bike_details, reverse= True))
print(sorted(bike_details.values()))
print(bike_details.items())

copy_bike_details = bike_details.copy()
print(copy_bike_details)
copy_bike_details.pop('engine displacement')
print(copy_bike_details)
copy_bike_details.popitem()
print(copy_bike_details)


dict_age = {"Ethan" : 4, "Sofia" : 50}
new_dict_age = {"Ethan" : 5, "Harper" : 58}

dict_age.update(new_dict_age)
print(dict_age)

del copy_bike_details
print(copy_bike_details)


