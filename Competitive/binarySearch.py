#!/usr/bin/python


def binary_search_index( array, low, high, key ):

    while low <= high:

        mid = ( low + high ) / 2

        if array[mid] > key :
            high = mid - 1

        elif array[mid] < key:
            low = mid + 1

        else:
            return mid

    return -1;



def partition( array, p, r ):

    i = p - 1
    j = p
    pivot = array[r]

    while j < r :
        
        if array[j] < pivot:
            i = i + 1
            swap( array, i, j )
    j += 1

    swap( array, i+1, r )

    return i+1;


def insertion_sort( array, p, r ):

    for i in xrange( p, r ):
        j = i - 1
        key = array[i]

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j+1] = key


def quick_sort( array, p, r ):

    if p < r:
        index = partition( array, p, r )

        quick_sort( array, p, index-1 )
        quick_sort( array, index+1, r )

if __name__ == "__main__":
    array = [ 10, 4, 2, 3, 29 , 43 ,6]

    insertion_sort( array, 0, len( array ) )
    
