sentence = "the quick brown fox jumped over the lazy dog with the quick and the dead"
words = sentence.split(" ")
set_of_words = set(words)
sorted_set_of_words = sorted(set_of_words)
print(" ".join(sorted_set_of_words))

num_dict = dict()
num_dict[1] = 1
num_dict[2] = 2 ** 2
num_dict[3] = 3 ** 2
print(num_dict)

string_1 = "Universal Hello"
string_2 = "Python"
set_1 = set(string_1)
set_2 = set(string_2)
common_char = set_1.intersection(set_2)
print("\nCommon letters: ", list(common_char))
