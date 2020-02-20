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

def dfs_recursive(graph, vertex, goal, path=[]):
    path += [vertex]
    if vertex=='g':
        print(path)
    for adjacent_vertices in graph[vertex]:
        if adjacent_vertices not in path:
            path = dfs_recursive(graph, adjacent_vertices,'g', path)
    return path
def dfs_recursive_shortest_path(graph, vertex, goal, path=[]):
    path += [vertex]
    if vertex == 'g':
        print(path)
    for adjacent_vertices in graph[vertex]:
        if adjacent_vertices not in path:
            path = dfs_recursive(graph, adjacent_vertices, 'g', path)
    return path


dfs_recursive(vertex_list, 's','g')
print("are the expanded states")
dfs_recursive_shortest_path(vertex_list,'s','g')
print("is the shortest path from start to goal")