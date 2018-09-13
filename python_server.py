#!/usr/bin/python

import socket
from threading import Thread,Lock
import python_thread
import sys
import signal
import os


server_addr = ( "192.168.1.109", 1800 )
server_handler = None

class logger():
	def __init__( self , filename ):
		self.filename = filename
		self.log_file = open( filename, "w" ) 
		self._redirect()

	def _redirect( self ):
		os.dup2( self.log_file.fileno(), sys.stdout.fileno() )



	def write_error( self, error_message ):
		pass

	def write_info( self, info_message ):
		pass


def _sigint_handler( sig, frame ):
	if server_handler != None:
		server_handler.close()

	

def set_signal_handlers():
	signal.signal( signal.SIGINT, _sigint_handler )


"""	
Starts a thread for each client when connection is established 
This thread receives messages from client, parses message and send it to 
the other client
"""
def start_server():
	global server_addr
	global server_handler

	server_handler = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

	server_handler.bind( server_addr )

	server_handler.listen( 10 )

	
	while True:
		conn,addr = server_handler.accept()
		client_thread = python_thread.ClientHandlerThread( conn, addr )
		client_thread.start()

		print "connection is established"
		sys.stdout.flush()
	#	sys.stdout.flush()
	#	t = Thread( target = connection_handler_thread, args = ( conn, addr ) )
	#	t.start()

def make_deamon():

	try:
		pid = os.fork()
		if pid > 0:
			sys.exit( 0 )

	except OSError, e:
		sys.stderr.write(" fork failed %d (%s)\n" %( e.errno, e.stderr ) )
		sys.exit( 1 )

	os.chdir( "/" )
	os.setsid()
	os.umask(0)

	try:
		pid = os.fork()
		if pid > 0:
			sys.exit(0)

	except OSError, e:
		pass



if __name__ == "__main__":
	make_deamon()
	log = logger( "/var/log/python_server.log" )
	set_signal_handlers()
	start_server()
