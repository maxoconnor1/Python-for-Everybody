import re
s = input("Please provide a file name:")
grep = input("Please provide a regular expression:")
fhand = open(s)
count = 0
for line in fhand:
    line = re.findall(grep, line)
    if len(line) > 0:
        count = count + 1

print(s ,"had", count, "lines that matched", grep )
