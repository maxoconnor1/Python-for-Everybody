import urllib.request
text = ''
charcount = 0
url = input("Provide a valid URL:")
fhand = urllib.request.urlopen(url)
for line in fhand:
    text = text + line.decode()
    charcount = charcount + len(text)

print(text[:3001])
print("There are, in total,", charcount, "characters in this text")

#'http://data.pr4e.org/romeo.txt'
