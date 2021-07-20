my_int = (10-4)*2
print(my_int)

colors = ["pink", "blue", "red"]
if "pink" in colors:
    print("this color is present in the list")
if "purple" not in colors:
    print("this color is not present in the list")

my_string = "hello"
my_list = list(my_string)
print(my_list)

score = "90.5"
if score >= "90":
    print("A grade")
elif score >= "80":
    print("B grade")
elif score >= "70":
    print("C grade")
elif score >= "50":
    print("D grade")

else:
    print("Fail")