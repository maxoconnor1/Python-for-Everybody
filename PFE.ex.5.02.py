largest = None
smallest = None
while True:

    num = input('Enter a number:')
    if num =='done':
        break
    try:
        intnum = int(num)
        if largest is None :
            largest = intnum
        elif intnum > largest :
            largest = intnum
        if smallest is None :
            smallest = intnum
        elif intnum < smallest :
            smallest = intnum
    except:
        print('Invalid input')
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
