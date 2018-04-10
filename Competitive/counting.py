MAX_ELEMENT = 100
def countingSort( arr ):
    counter = []
    for i in range( 0, MAX_ELEMENT ):
        counter.append( 0 )

    for i in range( 0, len( arr ) ):
        counter[arr[i]] = counter[arr[i]] + 1

    for i in range( 1, MAX_ELEMENT ):
        counter[i] = counter[i] + counter[i-1]

    return counter;

import sys

class Data:
    def __init__( self, number, string, index ):
        self.number = number
        self.string = string
        self.index = index

array_number = []
array_string = []

def getInput():
    sys.stdin.readline()
    index = 0
    for line in sys.stdin:
        line = line.strip("\n")
        position = line.index(' ')
        data = Data( int( line[0:position] ), line[position+1:] , index )
        index = index + 1
        array_number.append( int( line[0:position] ) )
        array_string.append( data )


def adjustArray( arr ):
    ordered_array = [None]*len( array_number )
    for i in range( len( array_number ) - 1, -1 , -1 ):
        ordered_array[arr[array_string[i].number] - 1] = array_string[i]

    return ordered_array

def printArray( arr ):
    for i in range( 0, len( arr ) ):
        if arr[i] is not None:
            if arr[i].index >= ( len( arr ) / 2 ):
                print arr[i].string,
            else:
                print "-",
    print ""
   

if __name__ == "__main__":
    getInput()
    arr = countingSort( array_number )
    arr2 = adjustArray( arr )
    printArray( arr2 )

