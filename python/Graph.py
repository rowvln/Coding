class Graph:
    def __init__(self):
        self.adjacencyList = {}
    def addVertex(self, vertex):
        if(not self.adjacencyList[vertex]):
            self.adjacencyList[vertex] = []
    def addEdge(self,vertex1, vertex2):
        self.adjacencyList[vertex1] = vertex2
        self.adjacencyList[vertex2] = vertex1
            

graph = Graph()
graph.addVertex("A")

print(graph)