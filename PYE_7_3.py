inpfile = input("Provide a file name:")
if inpfile == "na na boo boo":
    print("You have been punk'd!")
    quit()
count = 0
try:
    fhand = open(inpfile)

    for line in fhand:
        if line.startswith("Subject:"):
            count = count + 1
except:
    print("File cannot be opened:", inpfile)
    quit()

print("There were", count, "subject lines in", inpfile)
