#Count number of iterations
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print (zork, thing)
print('After', zork)

#Running total and total
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print('After', zork)

#Finding the average in a loop
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)

#Filter in a loop
print('Before')

for value in [9, 41, 12, 3, 74, 15] :
    if value > 20 :
        print('Large Number', value)
print('After')

#Search using a Boolean
found = False
print ('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
        break
    print(found, value)
print('After', found)

#Find the smallest Number
#'None' is a value that avoids the need to use arbitrary starting points
# 'is and is not are operators'
smallest_so_far = None
print('Before', smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if smallest_so_far is None :
        smallest_so_far = value
    elif the_num < smallest_so_far :
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('After', smallest_so_far)
