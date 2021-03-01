from socket import *

s = socket()

s.bind(('localhost',9999))
s.listen(3)

print("server is now opened")

while 1:
    c, addr = s.accept()
    print("connected with ",addr)
    print(c.recv(1024).decode())
    name = input("enter message" )
    c.send(bytes(name,'utf-8'))
    c.close()


