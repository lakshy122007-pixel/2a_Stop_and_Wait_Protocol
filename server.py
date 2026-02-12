import socket
from base64 import decode
from operator import truediv

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
s.bind(("localhost", 1234))         
s.listen(5)     
c, addr = s.accept()     
a=False

while not a:
    rep=c.recv(1024).decode('utf-8')
    if rep=='quit':
        a=True
    else:
        print(rep)
    c.send(input("Hello ").encode('utf-8'))

c.close()
s.close()