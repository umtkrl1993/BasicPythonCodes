
import os
import sys
from os.path import expanduser

from trie import *

class bookOperations:
    
    def __init__(self, book_name ):
        self._book_name = book_name + ".book"
        self._home_directory = expanduser( "~" )
        self._exact_file_path = self._home_directory + "/" + self._book_name
        self._file_handler = None 
        
    # This method just creates the file then closes the handler
    def __create_book(self):
        self._file_handler = open( self._exact_file_path, "w+" )
        self._file_handler.close()
        
    # This method opens the file , if the file does not exist first the file is created    
    def open_book(self):
        if not os.path.exists( self._exact_file_path ):
            self.__create_book()
            
        self._file_handler = open( self._exact_file_path, "a" )
            
    """
    It is assumed that file is already created but it isn't foolprof therefore a check for file's existence
    must be performed
    
    Before saving the word immediately check whether the word has already been saved
    """
    def save_word( self, new_word, meaning ):
        line = new_word + "->" + meaning + "\n"
        self._file_handler.write( line )
        
    def fill_cache(self):
        cache = trie()
        with open( self._exact_file_path, "r" ) as fh:
            for line in fh :
                ret = line.split("->")
                sys.stdout.write( str( ret[0] ) )
                sys.stdout.write( " " + str( len( ret[0] ) ) )
                sys.stdout.write("\n")
                cache.insert( ret[0] )
        
        
