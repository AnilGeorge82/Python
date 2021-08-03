for i in range (3):
    print("Hello")

for i in range( 2 ** 2):
    print("python")

for num in range(5, 10):
    print("number:", num)

for i in range(5, 8):
    print(i, "square is", i ** 2)
print("End of loop")

for val in range (5, 10 + 1):
    print(val)

print("the loop has ended")

x = range(5)

for i in reversed(x):
    print(i)

for i in reversed("welcome"):
    print(i)

print(list(range(5, 10, 1)))

x = list(range(5, 10, 2))
print(x)

print(tuple(range(5, -10, -2)))

start = -2
stop = -10
step = -2

for number in range (start, stop, step):
    print(number)