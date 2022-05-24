fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fhand = open(fname)
count = 0
for line in fhand :
    words = line.split()
    if len(words) == 0 or words[0] != "From" : continue
    if words[0] == "From":
        count = count + 1
        print(words[1])    
print("There were", count, "lines in the file with From as the first word")
