from socket import *
 
host = 'localhost' # '127.0.0.1' can also be used
port = 1242

 
s = socket()
photo = open('client1.jpg', 'wb')

s.connect ( ("localhost",port) )
  
packet = s.recv(1024)
while (packet):

  photo.write(packet)
  packet = s.recv(1024)
   
photo.close()
print 'end1'

print "Cliente1 recebeu o arquivo bucky.jpg"
s.close()
