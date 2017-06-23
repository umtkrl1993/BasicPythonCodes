#!/usr/bin/python

from Queue import Queue
from request import Request
import thread
import threading
import time
import ctypes

max_number_item = 10
requestQueue = Queue( max_number_item ) 
lock = threading.Lock()
SYS_gettid = 186
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def insertRequest( request ):
	lock.acquire()
	threadId = libc.syscall(SYS_gettid)
	print("Thread " + str( threading.current_thread() ) + " acquired the lock" )
	requestQueue.put( request )
	lock.release()

def shouldProcessRequest():
	print("Decider thread started with thread id " + str( threading.current_thread() ) )
	while True:
		if requestQueue.qsize() == max_number_item:
			processRequests()
		time.sleep(1)
		
def processRequests():
	while not requestQueue.empty():
		requestQueue.get().processRequest()
	

request = Request( "Dummy request" , "Get me" )

try:
	thread.start_new_thread( shouldProcessRequest,() )
except:
	print( "Thread error " + err )

while True:
	try:
		thread.start_new_thread( insertRequest, (request,) ) 
	except:
		print( "Thread error" + err )

	time.sleep(2)
		

