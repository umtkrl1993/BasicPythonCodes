#!/usr/bin/python

import DataHandler

class controller:
    
    def __init__(self):
        self._data_handler = DataHandler.dataHandler()
         
    def open_book(self, book_name ):
        self._data_handler.open_book( book_name )
            
    def save_word(self, new_word, meaning ):
        self._data_handler.save_word( new_word, meaning )
        
        
        
if __name__ == "__main__":
    print( "Starting controller")
    cont = controller()
    cont.open_book("Test2")
    cont.save_word("eschew", "sakinmak")
    cont.save_word("unnocious", "sefkat")
    
        
        
        
        