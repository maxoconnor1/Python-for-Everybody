import re
s = input("Please provide a file name:")
fhand = open(s)
count = 0
sum = 0

for line in fhand:
    numbers = re.findall('^New Revision: ([0-9]*)', line)
    if len(numbers) > 0:
        for number in numbers:
            count = count + 1
            sum = sum + int(number)
average = int(sum/count)
print(average)
