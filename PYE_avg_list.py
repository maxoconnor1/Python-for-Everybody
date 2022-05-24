
l = [] #Could also use l = list()
while True:
    userstr = input("Please provide a number: ")
    if userstr == "done" : break
    try:
        usernum = float(userstr)
        l.append(usernum)
    except:
        print("Provide a valid number")
        continue
print(len(l))
print(sum(l))
print(sum(l)/len(l))
