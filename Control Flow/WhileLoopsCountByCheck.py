start_num = 5
end_num = 150
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)

limit = 52

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)