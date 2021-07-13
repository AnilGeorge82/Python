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

list_str = ["Sofia", "Ella", "Samuel", "Ella", "Aiden", "Sofia"]
len_list_str = len(list_str)
len_set_str = len(set(list_str))
if len_list_str == len_set_str:
    print("There are no duplicate elements")
else:
    print("There are {} duplicate elements".format(len_list_str - len_set_str))

num_value = 51
print("The number stored in num_value is :", num_value)

if not num_value % 2 == 0:
    print("The number is an odd number")
else:
    print("The number is an even number")

