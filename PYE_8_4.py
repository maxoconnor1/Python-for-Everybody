shakespeare = "romeo.txt"
unqwords = list()
count = 0
fhand = open(shakespeare)
for line in fhand:
    words = line.split()
    for i in words:
        if i in unqwords : continue
        if i not in unqwords :
            newwords = unqwords.append(i)
unqwords.sort()
print(unqwords)
