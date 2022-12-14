

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = input("URL>")

def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False

for x in range(1,10000):
    if pscan(x):
        print("PORT =>", x , "is open")
    else:
        print("PORT =>", x , "is closed")