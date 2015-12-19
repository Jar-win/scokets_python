#!/usr/bin/env python

import socket               

SERVER_SOCKET = socket.socket()         
print "Socket created sucessfully @ {}".format(SERVER_SOCKET)
port = 12346

SERVER_SOCKET.bind(('', port))  #CREATE A WELCOMMING SOCKET | RETURNS NONE 
print "Socket binded to {}" .format(port)

SERVER_SOCKET.listen(5) #NUMBER OF QUEUED CONNECTIONS
print "Socket is listening..."

print "" #ForLineBreak            

while True:
   #PRINT THE OBJECT ADRESS TO SHOW IT'S CREATED FOR EVERY CLIENT

   NEW_CLIENT_SOCKET, addr = SERVER_SOCKET.accept() #CREATES A NEW SOCKET FOR THAT PERTICULAR CLIENT
   print 'Got connection from: {}'.format(addr[0])
   print "Created client socket @ %s",NEW_CLIENT_SOCKET
   '''
   NEW_CLIENT_SOCKET IS OF TYPE: 'socket._socketobject'
   addr is of type: <type 'tuple'>
   '''

   print 'Client info: {}'.format(addr) 
   send = NEW_CLIENT_SOCKET.send('Thank you for connecting') #RETURNS THE TOTAL NUMBER OF BYTES SENT
   print "Number of bytes sent: {}\n".format(send)
   # Close the connection with the client
   NEW_CLIENT_SOCKET.shutdown(1)
   NEW_CLIENT_SOCKET.close()


"""
SOME EXAMPLES OF OUTPUT:

Got connection from: 192.168.1.2
Created client socket @ %s <socket._socketobject object at 0x7f869d0ca980>
Client info: ('192.168.1.2', 51010)
Number of bytes sent: 24

Got connection from: 192.168.1.2
Created client socket @ %s <socket._socketobject object at 0x7f869d0ca910>
Client info: ('192.168.1.2', 51011)
Number of bytes sent: 24

Got connection from: 192.168.1.2
Created client socket @ %s <socket._socketobject object at 0x7f869d0ca980>
Client info: ('192.168.1.2', 51012)
Number of bytes sent: 24

Got connection from: 192.168.1.2
Created client socket @ %s <socket._socketobject object at 0x7f869d0ca910>
Client info: ('192.168.1.2', 51013)
Number of bytes sent: 24

Got connection from: 192.168.1.2
Created client socket @ %s <socket._socketobject object at 0x7f869d0ca980>
Client info: ('192.168.1.2', 51014)
Number of bytes sent: 24

Got connection from: 192.168.1.2
Created client socket @ %s <socket._socketobject object at 0x7f869d0ca910>
Client info: ('192.168.1.2', 51015)
Number of bytes sent: 24

Got connection from: 192.168.1.2
Created client socket @ %s <socket._socketobject object at 0x7f869d0ca980>
Client info: ('192.168.1.2', 51016)
Number of bytes sent: 24

"""