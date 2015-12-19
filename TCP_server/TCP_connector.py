#!/usr/bin/env python
import traceback
import socket
import sys

def socket_create():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print "Socket successfully created"
		return s
	except socket.error as err:
		print "socket creation failed with error {}".format(err)
		exit()

def connect(PORT=80, HOST="www.google.com"):
	s = socket_create()
	try:
		print "Attemptimg connection to {}...".format(HOST)
		host_ip = socket.gethostbyname(HOST)
		print "Connecting to {}...".format(host_ip)
	except socket.gaierror:
		# this means could not resolve the host
		print "there was an error resolving the host ({})".format(HOST)
		sys.exit()
	# connecting to the server
	s.connect((host_ip, PORT))
	print "The socket successfully connected to : {} on port: {}".format(host_ip, PORT)


def error_message():
	print '''
	USAGE: <script_name> arg1 arg2
	Where arg1 = Hostname
		  arg2 = Port number
	'''
def get_args():
	try:
		args = sys.argv
		#print len(args)
		if len(args) !=3:
			error_message()
			exit()
		if len(args) == 3:
			host = args[1]
			port = args[2]
			if int(port):
				connect(PORT=int(port), HOST=host)
			else:
				print "invalid port number"
	except:
		traceback.print_exc()

get_args()