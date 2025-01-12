# Queue datastructure
# Hans Snijders
#  04-12-2024

from Knoop1 import Knoop1

class Queue(object):
    def __init__(self ):
        '''initialiseert een nieuwe lege linked list als queue'''
        self.__root = None
        self.__tail = None

    # add data at the end of the queue
    def enQueue( self, data ):
        new_node = Knoop1(data, None)
        if self.__root is None:
            self.__root = new_node
            self.__tail = None
        else:
            self.__tail.setNext(new_node)
            self.__tail = new_node
        return data
        
    # remove the first element of the queue
    #   return the data value!    
    def deQueue( self ):
        if self.__root is None:
            return None
        data = self.__root.getData()
        self.__root = self.__root.getNext()
        if self.__root is None:
            self.__tail = None
        return data
 
    def print(self):
        '''drukt de data van de lijst in volgorde af'''
        wijzer = self.__root
        while wijzer != None:
            print(wijzer.getData(), end=' ')
            wijzer = wijzer.getNext()
        print()
