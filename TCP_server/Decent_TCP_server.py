#!/usr/bin/env python
# THIS WILL HAVE THE HONOR OF TAKING INPUT FROM USER
import socket

SERVER_SOCKET = socket.socket()
print "Socket created sucessfully @ {}".format(SERVER_SOCKET)
port = 12347

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
   
   CLIENT_INPUT = NEW_CLIENT_SOCKET.recv(10)
   print "Input: {}".format(CLIENT_INPUT)
   
   send = NEW_CLIENT_SOCKET.send('Thank you for connecting'+str(CLIENT_INPUT)) #RETURNS THE TOTAL NUMBER OF BYTES SENT
   print "Number of bytes sent: {}\n".format(send)
   # Close the connection with the client
   NEW_CLIENT_SOCKET.shutdown(1)
   NEW_CLIENT_SOCKET.close()
