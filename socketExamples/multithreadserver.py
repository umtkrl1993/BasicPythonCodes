#!/usr/bin/env python

import socket, threading

class ClientThread(threading.Thread):

    def __init__(self,ip,port, sock):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print "[+] New thread started for "+ip+":"+str(port)


    def run(self):    
        print "Connection from : "+ip+":"+str(port)

        sock.send("\nWelcome to the server\n\n")

        data = "dummydata"

        while len(data):
            data = sock.recv(2048)
            print "Client sent : "+data
            sock.send("You sent me : "+data)

        print "Client disconnected..."

host = "0.0.0.0"
port = 9999

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))
threads = []


while True:
    tcpsock.listen(4)
    print "\nListening for incoming connections..."
    (clientsock, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()