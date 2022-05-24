import socket
url = input("Please provide a URL:")
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
        print(data.decode(),end='')

    mysock.close()

except:
    import re
    urlcheck = re.findall('^http://.+/..+', url)
    if len(url) == 0:
        print ("You didn't provide a URL")
    elif len(urlcheck) == 0:
        print("You didn't provide a valid URL")
