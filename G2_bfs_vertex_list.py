#import the queue
import queue
#vertex list for the graph G1
vertex_list ={'s':['d','e','p'],
       'a':[],
       'b':['a'],
       'c':['a'],
       'd':['b','c','e'],
       'e':['h','r'],
       'f':['c','g'],
       'g':[],
       'h':['p','q'],
       'p':['q'],
       'q':[],
       'r':['f'] }

#function which gives the shortest path from source to destination as output
def bfs_shortest_path(vertex_list, start,dest ):
       #expanded vertices list
       expanded = []
       #queue to store various paths
       queue = [[start]]
       while queue:
              path1 = queue.pop(0)
              vertex = path1[-1]
              if vertex not in expanded:
                     #adjacent vertices to the given vertex
                     adjacent_vertices = vertex_list[vertex]
                     for node in adjacent_vertices:
                            path2 = list(path1)
                            path2.append(node)
                            queue.append(path2)
                            #if goal is reached return path
                            if node == dest:
                                   return path2
              #store the explored node in the expanded
              expanded.append(vertex)

#function to give expanded states
def bfs_states_expanded(vertex_list):
       expanded = []
       queue = ['s']
       #visted stores the node as soon as it is visited
       visited = ['s']
       while queue:
              vertex = queue.pop(0)
              #if a vertex is popped, then it is stores in expanded
              expanded.append(vertex)
              adjacent_vertices = vertex_list[vertex]
              for  node in adjacent_vertices:
                     #if any node is not visited append it in queue and visited
                     if node not in visited:
                            queue.append(node)
                            visited.append(node)
       #return the expanded list
       return expanded

#prints the expanded states
print("The states expanded are ", bfs_states_expanded(vertex_list)," in order")
#prints the shortest paths
print("The shortest path from start to the end is through ", bfs_shortest_path(vertex_list,'s', 'g') )

