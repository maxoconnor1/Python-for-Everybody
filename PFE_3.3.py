grade = input("Please provide a grade between 0 and 1:")
try:
     g = float(grade)
except:
    print("Please provide a numerical value only")
    quit()
if g < 0 or g > 1:
    print("The grade provided must be between 0 and 1")
    quit()
elif g >= 0.9:
    grade = "A"
elif g >= 0.8:
    grade = "B"
elif g >= 0.7:
    grade = "C"
elif g >= 0.6:
    grade = "D"
else:
    grade = "F"
print(grade)
