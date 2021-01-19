new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

name = "-".join(["Anil", "George"])
print(name)

letters = ['a', 'b', 'c', 'd', 'e']
letters.append('z')
print(letters)

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]
print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

names = ["Carol", "Anne", "Ben", "Donna"]
print(" & ".join(sorted(names)))
names.append("Eugenia")
print(sorted(names))