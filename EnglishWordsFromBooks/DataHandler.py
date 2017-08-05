#!/usr/bin/python


import FileUtility
from trie import *

class dataHandler:
    
    def __init__(self):
        self._cache = trie()
        self._book_handler = None
 
    """
    Method first should search for the word to see whether it is already in the file
    """   
    def save_word(self, new_word, meaning ):
        if ( not self._book_handler is None ) and ( not self._cache.search( new_word ) ):
            self._book_handler.save_word(new_word, meaning)
        
         
    def open_book(self, book_name ):
        self._book_handler = FileUtility.bookOperations( book_name )
        self._cache = self._book_handler.fill_cache()
        self._book_handler.open_book()
        
        
