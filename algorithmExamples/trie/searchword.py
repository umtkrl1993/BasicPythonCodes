#!/usr/bin/python

NUMBER_OF_LETTERS = 26


class trieNode:
    def __init__(self):
        self.children = []
        self.number_prefix = 0
        self.is_end = False
        for i in range( NUMBER_OF_LETTERS ):
            self.children.append( None )

class trie:
    def __init__( self ):
        self._root = trieNode()

    def insert( self, word ):
        current = self._root

        for i in range( len( word ) ):
            index = ord( word[i] ) - ord( 'a' )
            if current.children[index] == None:
                current.children[index] = trieNode()
            current.children[index].number_prefix = current.children[index].number_prefix + 1
            current = current.children[index]
        current.is_end = True
    """
    If is_end is not checked inside search function, it returns true even for substrings
    """
    def search( self, word ):
        current = self._root

        for i in range( len( word ) ):
            index = ord( word[i] ) - ord( 'a' )
            if current.children[index] == None:
                return False
            
            current = current.children[index]

        return current.is_end



searchEngine = trie()

searchEngine.insert( "umit" )
searchEngine.insert( "berke" )
searchEngine.insert( "aysegul" )

while True:
    val = raw_input( "Enter search word\n" )
    ret_val = searchEngine.search( val )
    if ret_val :
        print val + " is in the dictionary" 
    else:
        print val + " is NOT in the dictionary" 
