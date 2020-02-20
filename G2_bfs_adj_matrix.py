#import queue for the bfs implementation
import queue
#function which takes adjacent matrix, pairs and starting node as inputs and gives states expanded as output
def bfs_states_expanded(adj_mat,pair,start):
    #expanded states are stored
    expanded=[]
    #visited stores the visited nodes
    visited=[start]
    #path of bfs
    path=[start]
    while path:
        #pop out the first one in
        node=path.pop(0)
        #intialize value1 to zero
        value1=0;
        #search for the node in the given pairs
        for key,value in pair.items():
            #if found store the key
            if value==node:
                value1=key
        #find its adjoining vertices
        adj=adj_mat[value1]
        #append the node to the expanded list
        expanded.append(node)
        n=0
        while n<len(adj):
            if adj[n]==1 and pair[n] not in visited:
                visited.append(pair[n])
                path.append(pair[n])
            n+=1
    #returning the expanded list
    return expanded

#function to retur the shortest path by bfs
def bfs_shortest_path(adj_mat, start, goal,pair):
    visited= set()
    #queue to store various paths
    queue = [[start]]
    while(queue):
        path=queue.pop()
        node=path[-1]
        #if the node is goal
        if node==goal:
            return path
        #if not search for the value in key,value pairs
        if node not in visited:
            for key, value in pair.items():
                if value == node:
                    value1 = key
            #adjacent nodes to the given node
            adj = adj_mat[value1]
            length = 0
            #comparision to find the shortest path
            while length<len(adj):
                path2 = list(path)
                if adj[length]==1:
                    path2.append(pair[length])
                    queue.append(path2)
                length+=1


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
print("States Expanded are",bfs_states_expanded(adj_mat,pair,'s')," in order")
#prints the shortest path
print("shortest path from start to goal is through ",bfs_shortest_path(adj_mat,'s','g',pair))