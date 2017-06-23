#!/usr/bin/python


class Request:
	def __init__(self, requestName, request):
		self.requestName = requestName
		self.request = request

	
	def processRequest(self):
		print( " Starting to process request with name " + self.requestName )
		self.__process()


	def __process(self):
		print(self.request)
