names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
for name in names:
    usernames.append(name.lower().replace(" ", "_"))
print(usernames)

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")
print(usernames)

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
print(count)

items = ['first string', 'second string', 'third string', 'fourth string']
html_str = "<ul>\n"
for item in items:
    html_str += "<li>{}</li>\n".format(item)
    html_str += "</ul>"
print(html_str)

colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = []

for color in colors:
    lower_colors.append(color.lower())
print(lower_colors)
