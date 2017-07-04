#!/usr/bin/python

import socket
import sys
import threading
import thread
import time


class MultiThreadServer(object):

	__size__ = 1024

	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	def listen(self):
		self.sock.listen(5)
		print("Server started to listen the socket")
		while True:
			client, address = self.sock.accept()
			print("There is a connection with " + str(address))
			client.settimeout(60)
			threading.Thread(target = self.listenToClient, args = (client, address ))

	def listenToClient( self, client, address ):
		while True:
			try:
				data = client.recv(size)
				print("Received data is " + data )

			except:
				client.close()
				return False


if __name__ == "__main__":

	length = len(sys.argv)

	if length != 3 :
		print( "you should enter host and port number")
		sys.exit()
		
	host = sys.argv[1]

	port_number = sys.argv[2]

	try:
		port_number = int(port_number)

	except:
		print("Port number must be an integer")


	server = MultiThreadServer( str(host) , port_number)

	server.listen()
	



	
