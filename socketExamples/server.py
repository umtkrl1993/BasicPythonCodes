#!/usr/bin/python

import socket
import sys
import threading
import thread
import time

def createServerSocket( portNumber ) :
	sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
	server_address = ( 'localhost', portNumber )
	sock.bind( server_address )
	sock.listen(1)
	return sock


sock = createServerSocket( 10002 )

def listenerThread():
	try:
		while True:
			print >>sys.stdout, 'Waiting for a connection'
			connection, client_address = sock.accept();
			print >>sys.stdout, 'Connection is established with %s' %str(client_address)
			data = connection.recv( 100 )
			print("Data in listener thread is " + str(data))
			thread.start_new_thread( workerThread, ( data, client_address, ) )
		
	finally:
		connection.close()


def workerThread( data, client_address ):
	#print >> sys.stdout, " Data received from %s  is %s " % str(client_address), data
	print ( " Data received from client is " + str(data) )


if __name__ == "__main__" :
	listener = thread.start_new_thread( listenerThread(), () )	
	listener.join()




	
