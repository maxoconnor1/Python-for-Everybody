# Counting word occurence with a dictionary
word = 'brontosaurus'
d = dict()
for c in word :
    if c not in d :
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

#using Get method (takes a key and a default, returns corresponding value)
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d)

#romeo & juliet word counter - mine
fhand = open('romeo.txt')
poem = fhand.read()
words = poem.split()
romeodict = dict()
for word in words:
    romeodict[word] = romeodict.get(word, 0) + 1
print(romeodict)

#romeo & juliet word counter - textbook's
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    exit()
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word += 1]
print(counts)
