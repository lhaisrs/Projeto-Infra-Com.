import socket
clients={}
s = socket.socket()
host = socket.gethostname()
port = 12351
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    clients[addr] = c
    pressed = 0
    for eachsocket, eachaddrtuple in clients.iteritems():
        print 'receiving data from %s'%eachaddrtuple
        data = c.recv(1024)
        if data:
            print data
        pressed = pressed + 1
        print data, 'pressed count', pressed

