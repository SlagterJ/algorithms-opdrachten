#Stack  datastructure
#Hans Snijders
#04-12-2024

from Knoop1 import Knoop1

class Stack(object):
    def __init__(self):
        '''initialiseert een nieuwe lege linked list stack'''
        self.__root = None
        
    # add data to the stack        
    def push( self, data ):        
        new_node = Knoop1(data, None)
        if self.__root is None:
            self.__root = new_node
        else:
            new_node.setNext(self.__root)
            self.__root = new_node
        return data

    # remove the first element of the stack
    #   return the data value!        
    def pop( self ):
        if self.__root is None:
            return None
        data = self.__root.getData()
        self.__root = self.__root.getNext()
        return data
	
    def print(self):
        '''drukt de data van de lijst in volgorde af'''
        wijzer = self.__root
        while wijzer != None:
            print(wijzer.getData(), end=' ')
            wijzer = wijzer.getNext()
        print()
