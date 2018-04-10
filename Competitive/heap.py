
def swap( heap, p, r ):
    temp = heap[p]
    heap[p] = heap[r]
    heap[r] = temp


def minHeapify( heap, index, p, r ):
    min_index = index
    if p < len( heap ) and heap[p] < heap[min_index]:
        min_index = p
    if r < len( heap ) and heap[r] < heap[min_index]:
        min_index = r

    if min_index != index:
        swap( heap, min_index, index )
        minHeapify( heap, min_index, p, r )


def buildHeap( heap ):
    for i in range(0, len( heap ) / 2 ):
        minHeapify( heap, i , 0, len( heap ) - 1 )

def addElement( heap, element ):
    heap.append( element )
    buildHeap( heap )

def deleteElement( heap, element ):
    index = 0
    for i in range( 0, len( heap ) ):
        if heap[i] == element:
            index = i
            break

    swap( heap, index, len( heap ) - 1 )
    minHeapify( heap, index, 0, len( heap ) - 1 )

def printMin( heap ):
    print heap[0]

import sys

heap = [] 

def getInput():
    line = sys.stdin.readline().strip( "\n" )




