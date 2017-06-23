#!/usr/bin/python

import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10002 )

sock.connect(server_address)


try:
	while True:
		message = raw_input( "Please enter a message to server " )
		sock.sendall( message )

finally:
	sock.close()
 



