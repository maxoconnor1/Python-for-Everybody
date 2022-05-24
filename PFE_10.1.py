f = input("Please provide a file name:")
fhand = open(f)
names = dict()
for line in fhand:
    line = line.lower()
    words = line.split()
    if len(words) == 0 or words[0] != "from" : continue
    email = words[1]
    if words[0] == "from":
        # print(words) #debug
        if email not in names:
            names[email] = 1
        else:
            names[email] += 1

sortednames = list()
for key, value in list(names.items()):
    sortednames.append((value, key))

sortednames.sort(reverse = True)
print(sortednames[0])
