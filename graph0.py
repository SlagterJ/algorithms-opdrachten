from  graphLib import *

#define the graph:
#  grpah is a dictionary:
#   key:    vertex name
#   value:  list of connected vertices
g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
    }

#create the grap
graph = Graph(g)

#add edge from "k" to "f"
graph.add_edge( ("k", "f") )

#print all vertices
for vertice in graph:
    print(f"Edges of vertice {vertice}: ", graph.edges(vertice))

#print the graph
print( graph )

#create an empty graph
graph = Graph()

# read the graph data file
graph.readGraph( "Graph friends" )

#print the graph
print( graph )

# Test BFS traverse
print("\nBreadth-First Traverse starting from 'Anja':")
bfs_result = graph.bfs_traverse("Anja")
print(bfs_result)

# Test DFS traverse
print("\nDepth-First Traverse starting from 'Anja':")
dfs_result = graph.dfs_traverse("Anja")
print(dfs_result)

