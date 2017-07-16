#!/usr/bin/python

import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 10000 )
sock.connect(server_address)


try:
	while True:
		message = raw_input( "Please enter a message to server " )
		sock.sendall( message )

finally:
	sock.close()
 



