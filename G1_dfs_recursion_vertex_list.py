#the vertex-list for graph G1
vertex_list ={'s':['d','e','p'],
       'a':['b','c'],
       'b':['a','d'],
       'c':['a','d','f'],
       'd':['b','c','e','s'],
       'e':['d','s','h','r'],
       'f':['c','g','r'],
       'g':['f'],
       'h':['p','q','e'],
       'p':['s','h','q'],
       'q':['p','h'],
       'r':['e','f'] }
#The dfs function for the states expanded
def dfs_recursive(graph, vertex, goal, path=[]):
    #path of the graph
    path += [vertex]
    if vertex=='g':
        print(path)
        #traversing through the adjacent nodes
    for adjacent_vertices in graph[vertex]:
        if adjacent_vertices not in path:
            #new path including the adjacent nodes
            path = dfs_recursive(graph, adjacent_vertices,'g', path)
            #the final path
    return path
#function for the shortest path
def dfs_recursive_shortest_path(graph, vertex, goal, path=[]):
    #The path
    path += [vertex]
    if vertex == 'g':
        print(path)
    for adjacent_vertices in graph[vertex]:
        if adjacent_vertices not in path:
            #calling the function recursively
            path = dfs_recursive(graph, adjacent_vertices, 'g', path)
    return path


dfs_recursive(vertex_list, 's','g')
print("are the expanded states")
dfs_recursive_shortest_path(vertex_list,'s','g')
print("is the shortest path from start to goal")