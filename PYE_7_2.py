inpfile = input("Provide a file name:")
fhand = open(inpfile)
count = 0
fpvs = 0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence"):
        count = count + 1
        valuepos = (line.find(":"))
        valueslice = line[valuepos + 1:].rstrip()
        fpvs = fpvs + float(valueslice)

avg = fpvs/count
print("Average spam confidence:", avg)
