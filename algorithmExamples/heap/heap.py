#!/usr/bin/python
import pdb
from random import randint
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
        
array = [0,4,1,3,2,16,9,10,14,8,7]

print( "---------------------Before max-heapify array------------------------------" )

print array

print( "---------------------After build heap -------------------------------" )


build_heap( array )

print array


