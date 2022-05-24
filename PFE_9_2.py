raw = input("Please provide a file name: ")
fhand = open(raw)
DoWcount = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != "From" : continue
    DoW = words[2]
    if words[0] == 'From':
        if DoW not in DoWcount :
            DoWcount[DoW] = 1
        else:
            DoWcount[DoW] += 1
print(DoWcount)
