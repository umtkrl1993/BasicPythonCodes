#!/usr/bin/python

import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 1002 )
sock.connect(server_address)


try:
	while True:
		message = raw_input( "Please enter a message to server " )
		sock.sendall( message )

finally:
	sock.close()
 



