#!/usr/bin/env python

import socket

SERVER_ADRESS = '192.168.1.3'
SERVER_PORT = 7877

class Chat_server(object):

		def __init__(self):
				self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Created TCP socket
				print "Socket created"
				self.bind_server() 

		def bind_server(self):
				self.SOCKET.bind((SERVER_ADRESS, SERVER_PORT))
				print "Socket binded at {} on port {}".format(SERVER_ADRESS, SERVER_PORT)
				self.chat_loop()

		def chat_loop(self):
				try:
						self.SOCKET.listen(3)
						print "Socket is now listening..."
						while True:
								CLIENT1, address1 = self.SOCKET.accept()
								head  = CLIENT1.recv(150)
								print head
								if head[:4] == 'req@' :
										self.request(head, CLIENT1, address1)
										CLIENT1.close()
								elif head[:4] =='msg@':
										self.send_message(head, CLIENT1, address1)
										CLIENT1.close()                 
								else:
										print "-100@Invalid Header"
										CLIENT1.close()
				except KeyboardInterrupt:
						self.SOCKET.shutdown(0)
						self.SOCKET.close()
						print "\nSocket closed."

		def request(self, head, client1, address1):
				'''
				Server becomes client and askes the specified client for connection
				'''
				request_client_adress = head[4:head.index('|')].strip('\n')
				#print request_client_adress
				client_port_listen_port = 6969
				request_message = request_client_adress
				print "Requesting client {} for connection to {} on port {}".format(request_client_adress, address1, client_port_listen_port)
				request_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				request_client_socket((request_client_adress, client_port_listen_port))
				#add a try/catch clause here
				request_client_socket.send(request_message)

				response_message = request_client_socket.recv(10) #client will send response
				if response_message == 5:
					client1.send("1@PeerFound")






c1 = Chat_server()
