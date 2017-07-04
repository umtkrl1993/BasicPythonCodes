#!/usr/bin/python




class HashTable:

	def __init__(self, size):
		self.hashTable = [None]*size
		
	def _get_value(self, key):
		total = 0
		for i in range(len(key)):
			total += ord( key[i] ) * ( 7 * i )
		return ( len(key) * total ) % 256
	
	def insert(self, key):
		index = self._get_value(key)
		
		if self.hashTable[index] == None:
			self.hashTable[index] = key

		else:
			try:
				self.hashTable[index].append(key)

			except AttributeError:
				self.hashTable[index] = [self.hashTable, key]

	def delete(self, key):
		index = self._get_value(key)
		if self.hashTable[index] != None:
			if isinstance(self.hashTable[index], list ) :
				i = self.hashTable[index].index(key)
				self.hashTable[index][i] = None
			else:
				self.hashTable[index] = None		

	def lookup(self, key):
		index = self._get_value(key)
		isFound = False
		if isinstance(self.hashTable[index], list):
			isFound = key in self.hashTable[index]
		else:
			found = self.hashTable[index] == key			

		return isFound		
			
		
