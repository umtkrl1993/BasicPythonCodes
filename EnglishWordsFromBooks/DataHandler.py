#!/usr/bin/python


import FileUtility
from trie import *

class dataHandler:
    
    def save_word(self, book_name, new_word, meaning ):
        book_handler = FileUtility.bookOperations( book_name )
        
        book_handler.fillCache()