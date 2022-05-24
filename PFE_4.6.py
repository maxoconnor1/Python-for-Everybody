hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

def computepay(hours, rates):
    otrate = rates * 1.5
    if hours <= 40:
        grosspay = hours * rates
    else:
        grosspay = (40 * rates) + ((hours - 40) * otrate)
    return(grosspay)

gp = computepay(h, r)
print ("Pay", gp)
