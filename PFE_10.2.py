f = input("Please provide a file name: ")
fhand = open(f)
hours = dict()
for line in fhand:
    line = line.lower()
    words = line.split()
    if len(words) == 0 or words[0] != "from" : continue
    time = words[5]
    hour = time[time.find(':') - 2:time.find(':')]
    if words[0] == "from":
        if hour not in hours:
            hours[hour] = 1
        else:
            hours[hour] += 1

sortedhours = list()
for hour, count in list(hours.items()):
    sortedhours.append((hour, count))

sortedhours.sort(reverse=False)

for hour, count in sortedhours:
    print(hour, count)
