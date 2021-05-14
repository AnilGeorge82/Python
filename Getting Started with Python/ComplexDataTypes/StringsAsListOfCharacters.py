print('World')
x = 'World'
print(x)
print(x[0])
a, b, c, d, e = x
print(a)
print(c)
print(a, b, c, d, e)
a, b, _, _, _ = x
print(x)
print(b)

place = 'New York City'
print(place[-4:])
print(place[-4:-2])
print(place[4:-4])
print(place[0:8:2])
city = place[:8]
print(city)
del city