hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
print("Hours:", h, "Rate:", r)
otrate = r * 1.5
if h <= 40:
    grosspay = h * r
else:
    grosspay = (40 * r) + ((h - 40) * otrate)
print(grosspay)
