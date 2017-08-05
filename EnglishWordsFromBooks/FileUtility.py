
import os
from os.path import expanduser
class bookOperations:
    
    def __init__(self, book_name ):
        self._book_name = book_name + ".book"
        self._home_directory = expanduser( "~" )
        self._exact_file_path = self._home_directory + "/" + self._book_name 
        
        
    def __create_book(self):

        if not os.path.exists( self._exact_file_path ):                
            fh = open( self._exact_file_path, "w+" )
            fh.close()
        
    """
    It is assumed that file is already created but it isn't foolprof therefore a check for file's existence
    must be performed
    
    Before saving the word immediately check whether the word has already been saved
    """
    def save_word( self, new_word, meaning ):
        self.__create_book()
        fh = open( self._exact_file_path, "a")
        line = new_word + "->" + meaning
        fh.write( line )
        fh.close()
        
        
        
if __name__ == "__main__":
    obj = bookOperations("petcemetary")
    obj.save_word("sprouze", "growing")
        
    
    
