letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters) :
    print(i, letter)