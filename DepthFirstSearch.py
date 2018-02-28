class Graph:
    def __init__(self): #constructor for object Graph
        self.Vertices = set() #I use a set for the vertices, could just as well use list
        self.Edges = [] #list of edges
        self.AdjacencyList = {} #dictionary key is the vertex, values are the vertex neighbors
        self.VertexColor = {} #dictionary key is vertex, values are colors, will use these to check if vertex has been visited
    def addVertex(self, vertex):
        if vertex not in self.Vertices: #checks if vertex with label already exists
            self.Vertices.add(vertex) #adds vertex
            self.AdjacencyList[str(vertex)]=[] #creates a key for vertex
            self.VertexColor[str(vertex)] = 'black' #creates key for vertex and sets value to 'black'
    def addEdge(self, e):
        a = [e[0],e[1]] #dummy variable, probably unnecessary
        self.Edges.append(a) #appends edge to edge list
        self.AdjacencyList[str(e[0])].append(e[1]) #adds neighbor to vertex e(0)
        self.AdjacencyList[str(e[1])].append(e[0]) #adds neighbor to vertex e(1)
        
def DFS(G,V):
    G.VertexColor[str(V)]='red' #set root vertex color to red, meaning vertex has been visited
    tree = [[V]] #create tree with root, we will append list of vertices at each height
    neighbors = [] #create list for neighbors
    neighbors = neighbors + G.AdjacencyList[str(V)] #add root vertex neighbors to neighbors
    while neighbors != []: #I use a while loop that ends only when there are no vertices left to visit 
        tree_height =[] #creates a list of vertices for this height
        neighbors1 =[] #creates a list that will be populated with the neighbors of vertices at current height
        for i in neighbors: #go through the vertices 
            if G.VertexColor[str(i)]=='red': #if vertex color red, it has already been visited so we do nothing
                continue
            else:
                tree_height.append(i) #if vertex hasn't been visited add to current height
                G.VertexColor[str(i)]='red' #change the vertex color to 'red' as it has been visited
                neighbors1 = neighbors1 + G.AdjacencyList[str(i)] #add this vertex neighbors to new list that will be used for next height
        tree.append(tree_height) #append vertex list  to tree
        neighbors=neighbors1 #new set of neighbors to check
    tree.remove([])
    
    return tree
    
#create a graph object
g = Graph()
#number of vertices
n=8
#create each vertex in the graph, I use i+1 so vertex labels start at 1
for i in range(n):
    g.addVertex(i+1)

#define the edges of the graph
Edges = [[1,2],[1,4],[3,4],[5,4],[4,6],[7,8],[3,8]]
#add edges to the graph
for ed in Edges:
    g.addEdge(ed)

#call DFS algorithm to produce the lists of vertices at each height, rooted at vertex 1
tree = DFS(g,1)

#print the tree
print(tree)
#print the adjacency list
print(g.AdjacencyList)