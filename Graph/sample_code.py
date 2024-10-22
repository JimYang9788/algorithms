from collections import defaultdict




class Graph:

    def __init__(self):

        self.graph = defaultdict(list)


    def addEdge (self, u, v):
        self.graph[u].append(v)

    def DFSUtil (self, v, visited):

        visited[v] = True
        print ('visiting: ', v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # Uses a loop approach 
    def DFS (self, v):
        
        visited = [False] * (len (self.graph))

        self.DFSUtil(v, visited)


g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 


print (g.graph)
g.DFS(0)