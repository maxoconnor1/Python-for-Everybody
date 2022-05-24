userfile = input("Please provide a file name:")
fname = open(userfile)
for line in fname:
    line = line.upper().rstrip()
    print(line)
