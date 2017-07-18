#!/usr/bin/python
import pdb

def maxHeapify( heapArray, i ):
	largest = i
	left = 2*i 
	right = 2*i + 1

	if left < len( heapArray ) and heapArray[largest] < heapArray[left]:
		largest = left

	if right < len( heapArray ) and heapArray[largest] < heapArray[right]:
		largest = right

	if largest != i:
		temp = heapArray[largest]
		heapArray[largest] = heapArray[i]
		heapArray[i] = temp
		maxHeapify( heapArray, largest )


def build_heap( heapArray ):
	length = len( heapArray )
	count = 0
	bound = length / 2
	while count < bound:
		maxHeapify( heapArray, bound )
		bound = bound - 1

array = [0,4,1,3,2,16,9,10,14,8,7]

print( "---------------------Before max-heapify array------------------------------" )

#for a in array:
print array

print( "---------------------After build heap -------------------------------" )


build_heap( array )

print array


