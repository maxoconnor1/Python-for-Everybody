import re
s = input("Please provide a file name:")
fhand = open(s)
sum = 0

for line in fhand:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        for number in numbers:
            sum = sum + int(number)

print(sum)
