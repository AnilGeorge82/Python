for letter in "python":
    if letter == "o":

        break
    print(letter)

for letter in "python":
    print(letter)

    if letter == "o":

        break

for char in 'alpha':
    if char == 'c':
        print("The letter %s was found in the string" % char)
        break
else:
    print("The letter %s does not exist in the string" % char)

for num in [3, 11, 22, 35, 90]:
    print(num)

    if(num == 22):
        print("The number %d has been found" % num)
        print("Terminating the loop...")

        break