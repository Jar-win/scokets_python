#!/usr/bin/env python
# THIS WILL HAVE THE HONOR OF TAKING INPUT FROM USER
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
   
   CLIENT_INPUT = NEW_CLIENT_SOCKET.recv(10)
   print "Input: {}".format(CLIENT_INPUT)
   l = ""
   send = NEW_CLIENT_SOCKET.send('You sent: '+l+str(CLIENT_INPUT)) #RETURNS THE TOTAL NUMBER OF BYTES SENT
   print "Number of bytes sent: {}\n".format(send)
   # Close the connection with the client
   NEW_CLIENT_SOCKET.shutdown(1)
   NEW_CLIENT_SOCKET.close()


'''
#####
# OBSERVATION: When i created a client socket no other client was able to connect to it. unless the NEW_CLIENT_SOCKET was closed for the client and was started again for another client. 
####

jarwin@ubuntu:~/sockets/TCP_server$ ./Decent_TCP_server.py
Socket created sucessfully @ <socket._socketobject object at 0x7f67116308a0>
Socket binded to 12345
Socket is listening...

Got connection from: 192.168.1.2
Created client socket @ %s <socket._socketobject object at 0x7f6711630910>
Client info: ('192.168.1.2', 62766)
Input: GET / HTTP
Number of bytes sent: 34

OUTPUT: You sent: GET /HTTP
'''
