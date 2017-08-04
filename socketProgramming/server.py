#!/usr/bin/python



import socket
import sys
from thread import *
HOST = '127.0.0.1'
PORT = 8888


s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

try:
    s.bind( ( HOST, PORT ) )

except:
    print "Socket binding has failed"
    sys.exit(1)



s.listen(10)

def clientThread( conn ):
    while True:
        data = conn.recv( 1024 )
        conn.sendall( "OK.." )
        if data == "End":
            print "Ending connection ..."
            break
        print data


while 1:
    conn, addr = s.accept()

    start_new_thread( clientThread, ( conn, ) )

s.close()


