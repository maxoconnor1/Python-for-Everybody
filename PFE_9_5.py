raw = input("Please provide a file name: ")
fhand = open(raw)
domaincount = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != "From" : continue
    email = words[1]
    domain = email[email.find('@')+1:]
    if words[0] == 'From':
        if domain not in domaincount :
            domaincount[domain] = 1
        else:
            domaincount[domain] += 1
print(domaincount)
