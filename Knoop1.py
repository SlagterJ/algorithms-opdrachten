# Linked datastructures
# Jan Beumers
# 27-11-2020

# Knoop 1 is de basis voor lineaire structuren,
#         er is maar 1 pointerveld (next)
class Knoop1(object):
    def __init__(self, data, next):
        '''vult een nieuwe knoop met de gegeven data en verwijzing'''
        self.__data = data
        self.__next = next

    def getData(self):
        '''retourneert de data van de knoop'''
        return self.__data

    def setData(self, data):
        '''wijzigt de data van de knoop met de gegeven data'''
        self.__data = data

    def getNext(self):
        '''retourneert de verwijzing van de knoop'''
        return self.__next

    def setNext(self, next):
        '''wijzigt de verwijzing van de knoop met de gegeven verwijzing'''
        self.__next = next

    def print(self):
        print( "data:", self.__data, "next:", end = " " )
        if ( self.__next != None  ):
            print( self.__next.getData() )
        else:
            print( self.__next )
