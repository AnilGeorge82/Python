new_str = "The cow jumped over the moon"
new_str.split()
print(new_str)

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse,"\n")
print("Verse has a length of {} characters".format(len(verse)))
print("The first occurence of the word 'you' occurs in the {}th index.".format(verse.rfind('you')))
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))
print("The word 'being' occurs {} times in the verse.".format(verse.count('being')))
print("The first occurence of the word 'their' occurs in the {}th index.".format(verse.find('their')))