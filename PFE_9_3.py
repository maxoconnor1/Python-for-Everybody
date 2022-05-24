raw = input("Please provide a file name: ")
fhand = open(raw)
emailcount = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != "From" : continue
    email = words[1]
    if words[0] == 'From':
        if email not in emailcount :
            emailcount[email] = 1
        else:
            emailcount[email] += 1
print(emailcount)
