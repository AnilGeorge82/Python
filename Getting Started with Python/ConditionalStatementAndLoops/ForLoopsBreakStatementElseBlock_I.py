places = ["New Zealand", "Norway", "Botswana", "Zimbabwe", "Uzbekistan", "Paraguay"]

villan_at = "Mali"

for place in places:
    if place == villan_at:
        print("The villian has been captured")
        break
else:
    print("The villian got away :(")

places = ["New Zealand", "Norway", "Botswana", "Zimbabwe", "Uzbekistan", "Paraguay"]

villan_at = "Norway"

for place in places:
    if place == villan_at:
        print("The villian has been captured")
        break
else:
    print("The villian got away :(")

num = int(input("Enter a number: "))

for i in range(2, num//2)