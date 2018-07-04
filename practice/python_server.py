import socket
from threading import Thread,Lock
import sys

server_addr = ( "10.100.136.39", 1800 )

request_queue = []

request_mutex = Lock()


def connection_handler_thread( conn, addr ):
	data = conn.recv(1024)
	data = data + "-----" + "connection address " +str( addr )
	request_mutex.acquire()
	try:
		request_queue.append()

	finally:
		request_mutex.mutex.release()
	#sys.stdout.flush()
	#print data


def start_server():
	global server_addr

	server_handler = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

	server_handler.bind( server_addr )

	server_handler.listen(10)

	while True:
		conn,addr = server_handler.accept()
		print "connection is established"
		sys.stdout.flush()
		t = Thread( target = connection_handler_thread, args = ( conn, addr ) )
		t.start()


if __name__ == "__main__":
	start_server()
