import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Open the URL and apply the BS html parser
url = input("Enter -")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('span')
# Retrieve contents of tag
sumcontent = 0
# print(tags)
for tag in tags:
    content = int(tag.contents[0])
    sumcontent = sumcontent + content
    
print(sumcontent)     