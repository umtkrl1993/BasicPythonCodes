#!/usr/bin/python

import trie

search_structure = trie.trie()

def readAndInsertWords( filename ):

        fh = open( filename, "r" )
        name_list = fh.readlines()
        
        for name in name_list:
            name = name[ 0 : len(name)-1 ]  
            search_structure.insert( name )
        fh.close()

def searchWord( word ):
    return search_structure.search( word )

readAndInsertWords( "names.txt" )

if __name__ == "__main__":

    while True:
        word = raw_input( "Enter word to be searched\n")

        ret_val = searchWord( word )
    
        if ret_val :
            print word + " is in dictionary" 

        else:
            print word + " is NOT in dictionary" 

        print "--------------------------------------------------"
