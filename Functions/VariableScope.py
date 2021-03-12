egg_count = 0

def buy_eggs(count):
    return count + 12 # purchase a dozen eggs

egg_count = buy_eggs(egg_count)
print(egg_count)

str1 = 'Functions are important programming concepts.'

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()

str1 = 'Functions are important programming concepts.'

def print_fn():
    #str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn(str1)

str1 = 'Functions are important programming concepts.'

def print_fn():
    print(str1)

print_fn(str1)