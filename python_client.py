#!/usr/bin/python
import socket
import select
import sys
import json
import signal
import threading


inputs = [ sys.stdin ]

sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
sock_listen = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

outputs = []

remote_addr = ( "192.168.1.105", 1800 )

listen_addr = ( '', 2000 )

thread_controller = True

class Sender( threading.Thread ):

	def __init__( self ):
		threading.Thread.__init__( self )
		self.shutdown_flag = threading.Event()

	"""

	gets input from standart input 
	"""
	def message_sender( self ):
		print "sender thread started with id "

		try:
			sock.connect( remote_addr )
			inputs.append( sock )

			while self.shutdown_flag:
				print "waiting for i\o select"
				readable,writable,exceptional = select.select( inputs, outputs, inputs )

				for s in readable:
					if s is sock:
						print "socket is ready for reading"
						data = sock.recv( 1024 )
						print data
					else:
						print "stdin is ready for reading"
						line = sys.stdin.readline().strip("\n")
						message = {"name":"berke","message":line}
						message = json.dumps( message )
						print "message is %s" %message
						sock.send( message )

		except Exception as e:
			print str(e)

	def run( self ):
		self.message_sender()

class Receiver( threading.Thread ):

	def __init__( self ):
		threading.Thread.__init__( self )
		self.shutdown_flag = threading.Event()


	def message_receiver( self ):
		sock_listen.bind( listen_addr )
		sock_listen.listen( 10 )
		

		while self.shutdown_flag:
			conn, addr = sock_listen.accept()
			print "Message receiver conn accepted"
			data = conn.recv(1024)
			print "Received message is %s" %data

	def run( self ):

		print "Receiver thread has started"
		self.message_receiver()


def sigint_handler( sig, frame ):
	print "pressed ctrl c"
	raise ServiceExit

class ServiceExit( Exception ):
	pass

import time
if __name__ == "__main__":
	signal.signal( signal.SIGINT, sigint_handler )
	try:
		sender_thread = Sender()
		receiver_thread = Receiver()



		sender_thread.start()
		receiver_thread.start()

		while True:
			time.sleep(1)
	except ServiceExit:
		print "Service exit exception"
		receiver_thread.shutdown_flag.set()
		sender_thread.shutdown_flag.set()



