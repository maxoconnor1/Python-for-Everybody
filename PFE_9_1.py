#Stores words appearing in a file as keys in a dictionary, and assigns an incremental value.
fhand = open("words.txt")
contents = fhand.read()
# print(contents)
wordlist = contents.split()
# print(wordlist)
testdict = dict()
count = 0
for word in wordlist:
    count = count + 1
    testdict[word] = count
#print(testdict)
