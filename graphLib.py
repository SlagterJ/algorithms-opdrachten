""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""


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

    def edges(self, vertice):
        """ returns a list of all the edges of a vertice"""
        return self._graph_dict[vertice]
        
    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        return set(self._graph_dict.keys())

    def all_edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].append(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if [vertex, neighbour] not in edges:
                    edges.append([vertex, neighbour])
        return edges
    
    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def bfs_traverse(self, start_vertex):
        """
        Breadth-First Traverse algoritme
        Geeft vertices terug in de volgorde waarin ze bezocht worden
        """
        # Controleer of start_vertex bestaat
        if start_vertex not in self._graph_dict:
            return []
        
        # Initialiseer bezochte vertices en queue
        visited = set()
        queue = [start_vertex]
        traverse_order = []
        
        while queue:
            # Haal eerste vertex uit de queue
            current = queue.pop(0)
            
            # Als we deze vertex nog niet hebben bezocht
            if current not in visited:
                # Markeer als bezocht en voeg toe aan resultaat
                visited.add(current)
                traverse_order.append(current)
                
                # Voeg alle onbezochte buren toe aan de queue
                for neighbor in self._graph_dict[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return traverse_order

    def dfs_traverse(self, start_vertex):
        """
        Depth-First Traverse algoritme
        Geeft vertices terug in de volgorde waarin ze bezocht worden
        """
        # Controleer of start_vertex bestaat
        if start_vertex not in self._graph_dict:
            return []
        
        visited = set()
        traverse_order = []
        
        def dfs_recursive(vertex):
            # Markeer huidige vertex als bezocht en voeg toe aan resultaat
            visited.add(vertex)
            traverse_order.append(vertex)
            
            # Bezoek recursief alle onbezochte buren
            for neighbor in self._graph_dict[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        # Start de recursieve traverse
        dfs_recursive(start_vertex)
        return traverse_order

if __name__ == '__main__':

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }

    graph = Graph(g)

    for vertice in graph:
        print(f"Edges of vertice {vertice}: ", graph.edges(vertice))

    print( graph )

