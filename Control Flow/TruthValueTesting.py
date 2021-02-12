errors = 56
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")

weather = "snow"
if weather == "snow" or "rain":
    print("Wear Boots!")    

weather = "rain"
if weather == "snow" or "":
    print("Wear Boots!")  