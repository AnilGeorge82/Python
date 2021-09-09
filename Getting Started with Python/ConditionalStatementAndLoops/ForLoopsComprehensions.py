letters = [letter for letter in "anxiety"]
print(letters)

list_of_words = ["this", "is", "a", "list", "of", "words"]
items = [word[0] for word in list_of_words]
print(items)

items = [word[0].upper() for word in list_of_words]
print(items)

items = [word.upper() for word in list_of_words]
print(items)