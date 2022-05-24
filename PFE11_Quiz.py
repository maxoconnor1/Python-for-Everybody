import re
string = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
answer = re.findall('@(\S+)', string)
secondanswer = re.findall('\S+?@\S+', string)
print(answer)
print(secondanswer)

x = 'From: Using the : character'
y = re.findall('F.+:', x)
print(y)
