# Linked datastructures
# Jan Beumers
# 27-11-2020
# Hieronder volgen implementaties van de volgende klassen:
# Knoop2, BinarySearchTree


# Knoop 2 is de basis voor binaire bomen, er zijn 2 pointervelden (left, right)
class Knoop2(object):
    def __init__(self, data, left , right):
        '''vult een nieuwe knoop met de gegeven data en verwijzingen'''
        self.__data = data
        self.__left = left
        self.__right = right

    def getData(self):
        '''retourneert de data van de knoop'''
        return self.__data

    def setData(self, data):
        '''wijzigt de data van de knoop met de gegeven data'''
        self.__data = data

    def getLeft(self):
        '''retourneert de verwijzing van de knoop'''
        return self.__left

    def setLeft(self, left):
        '''wijzigt de verwijzing van de knoop met de gegeven verwijzing'''
        self.__left = left

    def getRight(self):
        '''retourneert de verwijzing van de knoop'''
        return self.__right

    def setRight(self, right):
        '''wijzigt de verwijzing van de knoop met de gegeven verwijzing'''
        self.__right = right

# hier volgen  recursieve hulpfuncties        
def printRecursief(wijzer):
    '''druk elke knoop af met zijn beide zonen'''
    if wijzer == None:
        return
    else:
        data = wijzer.getData()
        leftSon = wijzer.getLeft()
        rightSon = wijzer.getRight()
        print(data, end=' ')
        if leftSon != None:
            print(leftSon.getData(), end=' ')
        if rightSon != None:
            print(rightSon.getData(), end=' ')
        print()
        printRecursief(leftSon)
        printRecursief(rightSon)



class BinarySearchTree(object):
    def __init__(self):
        '''initialiseert een nieuwe binaire boom als een lege boom'''
        self.__root = None
        

    def voegToeIteratief(self, data):
        '''voegt een knoop toe aan de zoekboom'''
        knoop = Knoop2(data, None, None)
        if self.__root == None:
            self.__root = knoop
        else:
            wijzer = self.__root
            vorige = None
            while wijzer != None:
                vorige = wijzer
                if data <= wijzer.getData():
                    wijzer = wijzer.getLeft()
                else:
                    wijzer = wijzer.getRight()
            if data <= vorige.getData():
                vorige.setLeft(knoop)
            else:
                vorige.setRight(knoop)
    
    def voegToeRecursief(self, data):
        pass

    def preOrder(self):
        '''voert een pre-order traversie uit van de boom'''
        self._preOrder(self.__root)

    def _preOrder(self, wijzer):
        if wijzer is not None:
            print(wijzer.getData(), end=' ')
            self._preOrder(wijzer.getLeft())
            self._preOrder(wijzer.getRight())

    def inOrder(self):
        '''voert een in-order traversie uit van de boom'''
        self._inOrder(self.__root)

    def _inOrder(self, wijzer):
        if wijzer is not None:
            self._inOrder(wijzer.getLeft())
            print(wijzer.getData(), end=' ')
            self._inOrder(wijzer.getRight())

    def postOrder(self):
        '''voert een post-order traversie uit van de boom'''
        self._postOrder(self.__root)

    def _postOrder(self, wijzer):
        if wijzer is not None:
            self._postOrder(wijzer.getLeft())
            self._postOrder(wijzer.getRight())
            print(wijzer.getData(), end=' ')
        
    def zoekData(self, data):
        pass
    
    def zoekDataRecursief(self, data):
        pass

    def printBoom(self):
        printRecursief(self.__root)
        print("\npre order")
        self.preOrder()
        print("\nin order")
        self.inOrder()
        print("\npost order")
        self.postOrder()
  
# main program
# hier kunnen de methoden getest worden

BST = BinarySearchTree()
BST.voegToeIteratief(12)
BST.voegToeIteratief(16)
BST.voegToeIteratief(5)
BST.voegToeIteratief(8)
BST.voegToeIteratief(10)
BST.voegToeIteratief(14)
BST.voegToeIteratief(2)
print("\n\ iterarief" )
BST.printBoom()





