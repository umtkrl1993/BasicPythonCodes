#/usr/bin/python

import socket, sys
from thread import *

HOST = '127.0.0.1'
PORT = 80
ALLOWED_CONNECTION_NUMBER = 10

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    s.bind( ( HOST, PORT ) )
    s.listen( ALLOWED_CONNECTION_NUMBER )

except socket.error, msg:
    print "Could not open socket " + str( msg )
    sys.exit()


def httpRequestHandler( conn ):
    while True:
        data = conn.recv( 1024 )
        data = str(data).split( "\n" )
        url = data.split( " " )
        print "Requested url is " + url[1]
    conn.close()

def httpMessageParser( message ):
    

while True:
    conn,addr = s.accept()
    start_new_thread( httpRequestHandler, ( conn, ) )


