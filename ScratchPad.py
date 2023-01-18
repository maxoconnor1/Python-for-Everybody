import urllib.request, urllib.parse, urllib.error
x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
print(x)

import re
txt = "<p>Please click <a href=http://www.dr-chuck.com>here</a></p>"
rx = re.search("http://.*", txt)
print(rx)

txt = "<p>Please click <a href=http://www.dr-chuck.com>here</a></p>"
rx = re.search("href=.+", txt)
print(rx)

txt = "<p>Please click <a href=http://www.dr-chuck.com>here</a></p>"
rx = re.search("href=(.+)", txt)
print(rx)

txt = "<p>Please click <a href=http://www.dr-chuck.com>here</a></p>"
rx = re.search("<.*>", txt)
print(rx)