human_age = 30
if human_age < 0:
    print("Age must be a positive number.")
    exit()
if human_age <= 2:
    dog_age = human_age * 10.5

else:
    dog_age = 21 + (human_age - 2) * 4

print("The dog's age in dog years is", dog_age)

letter = 'b'
letter = letter.lower()
if letter in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." % letter)

elif letter == 'y':
    print("Y is ambiguous. It depends where it is used")

else:
    print("%s is a consonant." % letter)

month_name = "February"

if month_name == 'February':
    print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
    print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 days")
else:
    print("Give a correct month name")
