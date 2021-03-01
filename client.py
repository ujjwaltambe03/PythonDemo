from socket import *

from time import *

c = socket()

c.connect(('localhost',9999))

while 1:


    name = input("enter message" )
    c.send(bytes(name, 'utf-8'))
    sleep(5)
    print(c.recv(1024).decode())
