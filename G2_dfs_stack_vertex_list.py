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



def dfs(vertex_list, start):
    expanded = []
    stack = ['s']
    # visted stores the node as soon as it is visited
    visited = ['s']
    while stack:
        vertex = stack.pop(0)
        # if a vertex is popped, then it is stored in expanded
        expanded.append(vertex)
        adjacent_vertices = vertex_list[vertex]
        for i in adjacent_vertices:
            if i not in visited:
                stack.append(i)
                visited.append(i)
                break
    return expanded

def dfs_paths(vertex_list,start,goal):
        expanded = []
        stack = ['s']
        # visted stores the node as soon as it is visited
        visited = ['s']
        while stack:
            vertex = stack.pop(0)
            # if a vertex is popped, then it is stored in expanded
            expanded.append(vertex)
            adjacent_vertices = vertex_list[vertex]
            for i in adjacent_vertices:
                if i not in visited:
                    stack.append(i)
                    visited.append(i)
                    break
        return expanded


print(dfs(vertex_list, 's'))
print(dfs_paths(vertex_list,'s','g'))

