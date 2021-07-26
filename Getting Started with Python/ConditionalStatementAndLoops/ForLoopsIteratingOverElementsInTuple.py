for country in "Germany", "India", "Israel":
    print(country)

dogs = ("Pug", "Doberman", "Golden Retriever")
for dog in dogs:
    print("It's a", dog)

dog_weight = (("Pug", 20),
              ("Doberman", 80),
              ("Golden Retriever", 55))
for i, (dog, weight) in enumerate(dog_weight):
    print("The dog at index %d is a %s and it weighs %s pounds" %(i, dog, weight))

friends = ["John", "Sam", "Jill"]

for friend in friends:
    print("Happy New Year,", friend)
