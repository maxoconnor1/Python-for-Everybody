hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
otrate = r * 1.5
if h <= 40:
    grosspay = h * r
else:
    grosspay = (40 * r) + ((h - 40) * otrate)
print (grosspay)
