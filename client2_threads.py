#!usr/bin/python
from socket import *
 
host = 'localhost' # '127.0.0.1' can also be used
port = 52000
 
sock = socket()
#Connecting to socket
sock.connect((host, port)) #Connect takes tuple of host and port
 
#Infinite loop to keep client running.
while True:
    data = sock.recv(1024)
    print data
    sock.send('HI! I am client 2.')
 
sock.close()
