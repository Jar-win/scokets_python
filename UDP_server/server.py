#!/usr/bin/env python

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('192.168.1.3', serverPort))
print "The server is ready to receive on port: {}".format(serverPort)
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print clientAddress, message
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)

