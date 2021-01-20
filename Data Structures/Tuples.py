Egypt = (26.8206, 30.8025)
print(type(Egypt))
print("Egypt is at latitude: {}".format(Egypt[0]))
print("Egypt is at longitude: {}".format(Egypt[1]))

lbh = 56, 30, 100
length, breadth, height = lbh
print("The dimensions are {}*{}*{}".format(length, breadth, height))

tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])