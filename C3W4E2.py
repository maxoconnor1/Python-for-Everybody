urlprovided = input('Enter URL:')
count = int(input("Enter Count:"))
position = int(input("Enter Position:"))

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

currentcount = 0

#Loop through the pages at the URLs, capturing the URLs it contains and filtering out the relevant names


while currentcount <= count:
    
    html = urllib.request.urlopen(urlprovided, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    #print(tags)

    # Store all of the URLs within the URL provided, in order of appearance. 
    # Ordinality matches input position (starts from one)

    ord = 0
    urldict = dict()
    # urldict.update( {ord: urlprovided} )
   
    for tag in tags:
        ord = ord + 1
        urldict.update( {ord : tag.get('href', None)} )

    # print(urldict)

    # Retrieve just the relevant name from the relevant stored URL 

    currentname = re.findall("_[^by].*",urlprovided)
    stringname = currentname[0]
    cleanname = stringname[1:len(stringname) - 5]
    # print(stringname)
    # print(cleanname)

    # Increment the URL to search and count of URLs searched for the next loop

    urlprovided = urldict.get(position)
    
    currentcount = currentcount + 1

print(cleanname)