#!/usr/bin/python

import threading
import socket
import json


name_ip_map = {"berke":"192.168.1.108", "umit":"192.168.1.105" }



class ClientHandlerThread( threading.Thread ):

	def __init__( self, conn, addr ):
		threading.Thread.__init__( self )
		self.conn = conn
		self.addr = addr
		self.dummy_logger = None

	def _process_message( self , message ):
		parsed_message = json.loads( message )
		message_to_client = parsed_message['message']
		name = parsed_message['name']
		if not name in name_ip_map:
			self.dummy_logger.write( "name can not be found\n" )
			return -1

		target_ip = name_ip_map[name]
		complete_message = "Message from " + name + ":" + message_to_client
		self.dummy_logger.write( "complete message is created %s\n" %complete_message )
		remote_client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		remote_client.connect( ( target_ip, 2000 ) )
		self.dummy_logger.write( "Connection has established with remote\n")
		remote_client.send( complete_message )
		self.dummy_logger.write( "Mesasge has been send\n")
		remote_client.close()

	def run( self ):
		self.dummy_logger = open( "/home/umit/client.txt", "a" )
		while True:
			try:
				message = self.conn.recv( 1024 )
				if message == None:
					break
				self.dummy_logger.write( "Client addr is %s\n" %str( self.addr ) )
				self.dummy_logger.write( "Client message is %s\n\n" %str( message ) )
				self.dummy_logger.flush()
				self._process_message( message )
			except socket.error,e:
				print "Error receiving message from client %s" %str(e)
				self.dummy_logger.close()


