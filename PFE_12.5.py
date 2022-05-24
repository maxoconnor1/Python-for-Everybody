import socket
import re
url = input("Please provide a URL:")
text = ""
try:
spliturl = url.split("/")
hostname = spliturl[2]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((hostname, 80))
cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    text = text + data.decode()
#print(text)
paras = text.split("\r\n\r\n")
#print(len(paras))
body = paras[1]
header = paras[0]
print(body)
print(header)
mysock.close()

except:

    urlcheck = re.findall('^http://.+/..+', url)
    if len(url) == 0:
        print ("You didn't provide a URL")
    elif len(urlcheck) == 0:
        print("You didn't provide a valid URL")
    else:
        print("Unknown error")
