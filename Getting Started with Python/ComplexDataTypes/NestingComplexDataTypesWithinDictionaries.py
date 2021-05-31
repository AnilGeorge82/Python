fruit_qty = {}
print(fruit_qty)

fruit_qty['Banana'] = 50
fruit_qty['Apple'] = 78
fruit_qty['Apricot'] = 40

print(fruit_qty)

fruit_qty['Orange'] = 70
fruit_qty['Avocado'] = 30

print(fruit_qty)

print(fruit_qty['Apricot'])


fruit_qty['Watermelon'] = 10
print(fruit_qty)

fruit_qty_consumed = {'Banana' : [50, 60, 40, 55],
                      'Apple'  : [78, 86, 80, 60],
                      'Apricot': [40, 70, 30, 55],
                      'Orange' : [70, 80, 60, 65],
                      'Avocado': [30, 50, 40, 45]}

print(fruit_qty_consumed)
print(fruit_qty_consumed['Orange'])
print(fruit_qty_consumed['Orange'][3])
print(fruit_qty_consumed['Avocado'])
fruit_qty_consumed['Avocado'][3] = 50
print(fruit_qty_consumed['Avocado'])

fruit_qty_consumed = {'Banana' : {'Fri' : 70, 'Sat' : 80, 'Sun' : 95},
                      'Apple'  : {'Fri' : 90, 'Sat' : 95, 'Sun' : 110},
                      'Apricot': {'Fri' : 70, 'Sat' : 85, 'Sun' : 95},
                      'Orange' : {'Fri' : 80, 'Sat' : 90, 'Sun' : 100},
                      'Avocado': {'Fri' : 60, 'Sat' : 70, 'Sun' : 80}}
print(fruit_qty_consumed)
print(fruit_qty_consumed['Orange'])
print(fruit_qty_consumed['Avocado']['Sun'])
print(fruit_qty_consumed['Apricot']['Sat'])


