import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("localhost",1234))
a=False

while not a:
    c.send(input("Hello ").encode('utf-8'))
    rep=c.rec(1024).decode('utf-8')

    if a=='quit':
        a=True
    else:
        print(rep)
c.close()