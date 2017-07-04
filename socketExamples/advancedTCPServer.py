#!/usr/bin/python

import socket
import threading
import SocketServer

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		data = str(self.request.recv(1024))
		print("Received data is " + data )


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass



if __name__ == "__main__":
	HOST,PORT="192.168.1.109", 10000
	server = ThreadedTCPServer((HOST,PORT), ThreadedTCPRequestHandler)
	ip, port = server.server_address

	server_thread = threading.Thread(target=server.serve_forever)

	server_thread.daemon = True
	server_thread.start()
	print("Server loop running in thread:", server_thread.name)


