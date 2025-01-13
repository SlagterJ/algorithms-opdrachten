""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""

# import your implementation of the Stack and Queue
from Stack import Stack
from Queue import Queue

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict
        
    def readGraph( self, filePath ):
        inputFile = open( filePath, 'r')
        data = str()
        iRegel = 0
        for regel in inputFile:
            if ( iRegel > 0 ): data += ", "
            data += regel.strip()
            iRegel += 1
        inputFile.close()

        self._graph_dict  = eval( "{" + data + "}")

    def connected_to(self, vertice):
        """ returns a list of all connected vertici"""
        return self._graph_dict[vertice]

    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        return set(self._graph_dict.keys())

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge, Gericht=True):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        #edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        if not Gericht:
            t = [(vertex1, vertex2), (vertex2, vertex1)]
        else:
            t = [(vertex1, vertex2)]
        for x, y in t:
            if x in self._graph_dict:
                self._graph_dict[x].append(y)
            else:
                self._graph_dict[x] = [y]
   
    def __str__(self):
        res = ""
        for vertex, connected in self._graph_dict.items():
            res += "vertex: "+ str(vertex) + " "
            res += "connected to: "
            for c in connected:
                res += str(c) + " "
            res += "\n"
        return res

    def BFT( self, startVertex ):
        # return a list
        vertex_list = list()

        queue = Queue()
        queue.enQueue(startVertex)
        
        while True:
            vertex = queue.deQueue()
            if vertex is None:
                break

            if vertex not in vertex_list:
                vertex_list.append(vertex)
                for connected in self._graph_dict[vertex]:
                    queue.enQueue(connected)


        return( vertex_list ) 
 
    def DFT( self, startVertex ):
        # return a list
        vertex_list = list()

        stack = Stack()
        stack.push(startVertex)
        
        while True:
            vertex = stack.pop()
            if vertex is None:
                break
                
            if vertex not in vertex_list:
                vertex_list.append(vertex)
                for connected in reversed(self._graph_dict[vertex]):
                    stack.push(connected)

        return( vertex_list ) 
 

if __name__ == '__main__':

    friends = Graph()
    friends.readGraph( "Path to This file: Graph friends" )
    print( friends )
    startVertex = "Anja"
    print( "The BFT from", startVertex, "is", friends.BFT( startVertex ) )
    print( "The DFT from", startVertex, "is", friends.DFT( startVertex ) )
