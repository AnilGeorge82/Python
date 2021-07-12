cars_list = ["Toyota Camry", "Honda Accord", "Honda Civic", "Toyota Corolla"]
print("List of cars before the swap:", cars_list)
cars_list_temp = cars_list[0]
cars_list[0] = cars_list[2]
cars_list[2] = cars_list_temp
print("List of cars after the swap: ", cars_list)

list_student = ["Sofia", "Ella", "Samuel", "Ella", "Aiden", "Sofia"]
print("Student list: ", list_student)
print("Number of students: ", len(list_student))
student_set = set(list_student)
print("\nNew student list: ", list(student_set))
print("Length of modified student list: ", len(student_set))
print("There are %s duplicate elements"%(len(list_student) - len(student_set)))