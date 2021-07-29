student_scores = {'John' : 80,
                  'Sam'  : 60,
                  'Jill' : 50,
                  'Bob'  : 96}
for student, score in student_scores.items():
    print("Student:", student, "\tScore:", score)

numbers = [4, 6, 7, 89]

for num in numbers:
    quotient = num // 2

    print(quotient, "is the quotient of", num, "/ 2")

mixed_list = [145, 10.5, 1+3j, True, "Python", (0, 1), [2, -5], {"Class":"V", "Section":"A"}]
for item in mixed_list:
    print("Type of ", item, " is ", type(item))

num_list = [2, 4, 6, 8, 4294967296]

square = 0

for val in num_list:
    square = val ** 2

    print("Square of", val, "is", square)

string = "Anil George"
count = 0
for i in string:
    count = count + 1
print(count)

numbers = [2, 3, 5, 7]

for num in numbers:
    print(num)

else:
    print("No more items left in the list.")

characters = {"a", "b", "c", "d", "e"}

for letter in characters:
    print(letter)
else:
    print("No more characters left")