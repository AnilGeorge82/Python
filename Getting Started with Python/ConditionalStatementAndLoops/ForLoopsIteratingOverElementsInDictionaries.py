student_scores = {'John' : 80,
                  'Sam'  : 60,
                  'Jill' : 50,
                  'Bob'  : 96}

print(student_scores)

for student in student_scores:
    print(student)

for score in student_scores.values():
    print(score)

for key in student_scores:
    print("Key value pair -", key, ":", student_scores[key])

for key_value in student_scores.items():
    print(key_value)

for student, score in student_scores.items():
    print("Student:", student, "\tScore:", score)
