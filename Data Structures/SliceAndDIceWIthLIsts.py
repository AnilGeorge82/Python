months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
q3 = months[6:9]
print(q3)
second_half = months[:6]
print(second_half)
second_qrtr = months[3:6]
print(second_qrtr)

# mutable
months[0] = "Monday"
print(months)
# immutable - strings arent mutable
greeting = "Hello there"
greeting[0] = 'm'
print(greeting)
