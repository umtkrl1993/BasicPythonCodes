
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


	def printList(self):
		current=self._head.getNext()
		while not current is None:
			element=current.getElement()
			print "\n" + str(element)
			current=current.getNext()




liste=linkedlist()
liste.prepend("umit aykurt")
liste.prepend("berkay aykurt")
liste.prepend("berke aykurt")
liste.prepend("burak aykurt")

liste.printList()
		
