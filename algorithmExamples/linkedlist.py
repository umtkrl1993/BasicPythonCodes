class listnode:
	def __init__(self, element=None, nextNode=None):
		self._element=element
		self._nextNode=nextNode
			
	def setNext(self, nextNode):
		self._nextNode=nextNode

	def getNext(self):
		return self._nextNode

	def getElement(self):
		return self._element


class linkedlist:
	def __init__(self):
		self._head=listnode()
		self._size=0

	def prepend(self, element):
		current=self._head.getNext()
		newNode=listnode(element,current)
		self._head.setNext(newNode)
		self._size +=1
	
	def append(self, element):
		current = self._head.getNext()
		previous = current	
		while not current is None:
			previous = current
			current = current.getNext()

		newNode = listnode(element,current)
		self._size += 1

		if previous is None:
			self._head.setNext( newNode )
			return 
		previous.setNext( newNode )

	def reverse(self):
		current = self._head.getNext()
		current_next = current.getNext()
		current_next2 = current_next.getNext()

		while not current_next2 is None:
			current_next.setNext( current )
			current = current_next
			current_next = current_next2
			current_next2 = current_next2.getNext()

		self._head.setNext( current_next )
		
		
	def clear(self):
		del self._head
		self._head = listnode()
		"""
		find a way to clear the list !!
		"""
		
	def printList(self):
		current=self._head.getNext()
		while not current is None:
			element=current.getElement()
			print str(element) + "\n"
			current=current.getNext()

liste=linkedlist()

member = ["umit aykurt", "aysegul aykurt", "berke aykurt", "berkay aykurt", "burak aykurt"]

print( " ---------------------List elements in order-----------------------------------------------\n" )

for mem in member:
	liste.prepend( mem )

liste.printList()

liste.reverse()

print( "---------------------List elements in reverse order-----------------------------------------\n" )

liste.printList()
'''
liste.clear()

print( " ---------------------List elements in order-------------------------------------------------------\n" )

for mem in member:
	liste.append( mem )

liste.printList()	
'''
