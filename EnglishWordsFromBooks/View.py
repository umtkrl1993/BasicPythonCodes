#!/usr/bin/python

import Controller
import sys
import OptionsDefinitions

class view:
    
    def __init__(self, controller = None):
        if controller is None:
            self._controller = Controller.controller()
            
        else:
            self._controller = controller

            
    def start_stream(self):
        selection = ""
        while True:
            print( "Enter a book name")
            print( "Type quit to exit the program")
            selection = raw_input()
            
            if selection == "quit":
                sys.exit(0)
                
            else:
                self.save_word( selection )
            
        """
        Instead of saving each word as soon as getting the input , the words could be inserted into a list and 
        saved altogether
        """
    def save_word( self,book_name ):
        print( "Press 1 to enter a new book or ")
        self._controller.open_book(book_name)
        while True:
            new_word = raw_input("Enter word\n")
            if new_word == "1":
                break
            meaning = raw_input("Enter meaning\n")
            if not self._controller is None:
                self._controller.save_word( new_word, meaning )
    
                   
            
if __name__ == "__main__":
    starter = view()
    starter.start_stream()
        
        
            
            
        