#for loops are ideal when the number of iterations is known or finite.

#Examples:

#When you have an iterable collection (list, string, set, tuple, dictionary)
#for name in names:
#When you want to iterate through a loop for a definite number of times, using range()
#for i in range(5):

#while loops are ideal when the iterations need to continue until a condition is met.

#Examples:

#When you want to use comparison operators
#while count <= 100:
#When you want to loop based on receiving specific user input.
#while user_input == 'y':

num_list = [422, 136, 524, 85, 96, 719, 5, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list):
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print("The numbers of odd numbers added are: {}".format(count_odd))
print("The sum of the odd numbers added is: {}".format(list_sum))