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

num = 26

for i in range(2, num//2):
    if num % i == 0:
        print("It is not a prime number")
        break
else:
    print(num, "is a prime number")

for i in range(3):
    password = "secret"

    if password == "secret":
        print("you guessed the password :)")
        break
else:
    print("3 incorrect password attempts")