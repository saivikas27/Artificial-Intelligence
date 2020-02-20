def dfs_recursive(graph, pair,vertex, goal, path=[]):
    path += [vertex]
    if vertex == 'g':
        print(path)
        node = vertex
        # intialize value1 to zero
        value1 = 0;
        # search for the node in the given pairs
        for key, value in pair.items():
            # if found store the key
            if value == node:
                value1 = key
        # find its adjoining vertices
        adj = adj_mat[value1]
        # append the node to the expanded list
        n = 0
        while n < len(adj):
            if adj[n] == 1 and pair[n] not in path:
                path = dfs_recursive(graph, pair, pair[n], 'g', path)
            n += 1
    return path
#key pairs for each and every value
pair={0:'s',1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'p',10:'q',11:'r'}
#adjacent matrix for the given directed and unweighted graph
adj_mat=[[0,0,0,0,1,1,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,1,0,0,0,0,0,0,0,0,0,0],
         [0,1,0,0,0,0,0,0,0,0,0,0],
         [0,0,1,1,0,1,0,0,0,0,0,0],
         [0,0,0,0,1,0,0,0,1,0,0,1],
         [0,0,0,1,0,0,0,1,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,1,1,0],
         [0,0,0,0,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,1,0,0,0,0,0]]

#prints the states expanded
print("States Expanded are",dfs_recursive(adj_mat,pair,'s','g')," in order")
#prints the shortest path
#print("shortest path from start to goal is through ",dfs_shortest_path(adj_mat,'s','g',pair))