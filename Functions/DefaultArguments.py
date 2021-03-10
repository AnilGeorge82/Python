def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2


print(cylinder_volume(10, 5))
print(cylinder_volume(10))
# However, if we call cylinder_volume(10, 7) the 7 will simply overwrite the default value of 5.
print(cylinder_volume(10, 7))

# Population Density Function
def population_density(population, land_area):
    return population/land_area
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

def readable_timedelta(days):
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)
print(readable_timedelta(100))
