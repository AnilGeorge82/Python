sentence = "the quick brown fox jumped over the lazy dog with the quick and the dead"
words = sentence.split(" ")
set_of_words = set(words)
sorted_set_of_words = sorted(set_of_words)
print(" ".join(sorted_set_of_words))

num_dict = dict()
num_dict[1] = 1
num_dict[2] = 2 ** 2
num_dict[3] = 3 ** 2
print(num_dict)

string_1 = "Universal Hello"
string_2 = "Python"
set_1 = set(string_1)
set_2 = set(string_2)
common_char = set_1.intersection(set_2)
print("\nCommon letters: ", list(common_char))

list_num = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
len_of_list = len(list_num)
print("Numbers before slicing: %s" %list_num)
print("Length of numbers before slicing: ", len_of_list)

half = int(len_of_list / 2)

list_num1 = list_num[ :half]
list_num2 = list_num[half: ]

print("\nFirst half: %s" %list_num1)
print("Second half: %s" %list_num2)

var = 223456789.96869786859
if(type(var) == int):
    print("Type of the variable is Integer")

elif(type(var) == float):
    print("Type of the variable is Float")

elif(type(var) == complex):
    print("Type of the variable is Complex")
else:
    print("Type of the variable is Unknown")

num1 = 12

operator = "*"

num2 = 5

if operator == "+":
    print("Addition: ", num1 + num2)
if operator == "-":
    print("Substraction: ", num1 - num2)
if operator == "*":
    print("Multiplication: ", num1 * num2)
if operator == "/":
    print("Division: ", num1 / num2)
else:
    print("This is not a valid operator")

num_1 = 50

if num_1 % 5 == 0 and num_1 % 7 == 0:
    print("This number is divisible by both 5 and 7")
elif num_1 % 5 == 0:
    print("This number is divisible by 5")
elif num_1 % 7 == 0:
    print("This number is divisible by 7")
else: 
    print("This number is neither divisible by 5 nor 7")



