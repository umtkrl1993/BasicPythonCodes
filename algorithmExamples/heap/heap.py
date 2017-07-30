#!/usr/bin/python
def maxHeapify( heapArray, heapSize,i ):
	largest = i
	left = 2*i 
	right = 2*i + 1

	if left < heapSize and heapArray[largest] < heapArray[left]:
		largest = left

	if right < heapSize and heapArray[largest] < heapArray[right]:
		largest = right

	if largest != i:
		temp = heapArray[largest]
		heapArray[largest] = heapArray[i]
		heapArray[i] = temp
		maxHeapify( heapArray, heapSize ,largest )

def build_heap( heapArray ):
	length = len( heapArray )
	count = 0
	bound = length / 2
	while count < bound:
		maxHeapify( heapArray, length, bound )
		bound = bound - 1

def heap_sort( heapArray ):
        heapSize = len( heapArray )
        build_heap( heapArray )
        length = heapSize
        counter = 2
        while length > counter:
                temp = heapArray[1]
                heapArray[1] = heapArray[heapSize-1]
                heapArray[ heapSize - 1 ] = temp
                heapSize = heapSize - 1
                length = length - 1
                maxHeapify( heapArray, heapSize, 1 )
        

