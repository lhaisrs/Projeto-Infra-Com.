import socket 

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12351
s.connect((host, port))

while True:
    print "sending to"
    s.send('sent by 2'+ host)
