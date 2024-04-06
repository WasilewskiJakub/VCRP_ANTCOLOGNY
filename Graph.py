import random
#Module holds graph representation

class Vertex:
    def __init__(self, val) -> None:
        self.val = val
        pass

class Edge:
    def __init__(self, v1, v2, edge_weight) -> None:
        self.v1 = v1
        self.v2 = v2
        self.edge_weight = edge_weight
        pass

class Graph:
    
    def __init__(self, size) -> None:
        self.vertex = [0]
        self.size = size + 1
        self.edges = [[0] * self.size for _ in range(self.size)]
        # lista przedstawia zapotrzebowanie dla konkretnego klienta
        for i in range(size):
            self.vertex.append(random.randint(1,50))
        
        for i in range(self.size):
            for j in range(i, self.size):
                edge_weight = 0 if i == j else random.randint(5,30)
                self.edges[i][j] = edge_weight
                self.edges[j][i] = edge_weight              
        pass
    
    def neighbors(self,v):
        neighbors_list =[]
        for index,_ in enumerate(self.edges[v]):
            if index != v:
                neighbors_list.append(index)
        return neighbors_list
    
    def printGraph(self):
        print("Vertex:",self.vertex)
        print("Edges:")
        for row in self.edges:
            print(row)
        pass