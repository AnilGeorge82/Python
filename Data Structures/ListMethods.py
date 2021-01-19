name = 'jim'
student = name
name = 'tim'
print(name)
print(student)

scores = ["B", "C", "A", "D", "B", "A"]
grades = scores
print("scores: "+ str(scores))
print("grades: "+ str(grades))
scores[3] = "E"
print("scores: "+ str(scores))
print("grades: "+ str(grades))

batch_sizes = [150, 6, 78, 89, 45, 88, 34]
print(max(batch_sizes))
print(sorted(batch_sizes))
print(sorted(batch_sizes, reverse=True))

python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python']
print(max(python_varieties))
print(sorted(python_varieties))
print(sorted(python_varieties, reverse=True))