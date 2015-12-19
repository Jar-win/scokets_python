#!/usr/bin/env python
import socket

s = socket.socket()

port = 12346
ADRESS = '192.168.1.3'
SEND = raw_input('Enter data to be sent: ')

s.connect((ADRESS, port))
s.send(SEND)
# receive data from the server
while True:
  data = s.recv(1)
  print "{} => {} ({})".format(data, len(data), type(data))
  if len(data) < 1:
    break

# close the connection
s.close()




