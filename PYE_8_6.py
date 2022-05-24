tally = list()
while True :
    val = input("Please provide a number: ")
    if val == "done":
        break
    try:
        fval = float(val)
        tally.append(fval)
    except:
        print('Invalid Input')
        continue
print("Maximum:", max(tally))
print("Minimum:", min(tally))


# while True :
    #sval = input('Enter a number:')
    #if sval == 'done':
        #break
    #try:
        #fval = float(sval)
    #except:
        #print('Invalid Output')
        #continue
        #print(fval)
