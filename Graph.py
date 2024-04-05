import random

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
    def __init__(self, vertex_n) -> None:
        self.vertex_list = []
        self.edge_set = []
        for i in range(vertex_n):
            self.vertex_list.append(Vertex(random.randint(1,50)))
        for i in range(vertex_n):
            for j in range(i + 1, vertex_n):
                edge_weight = random.randint(1,30)
                self.edge_set.append(Edge(self.vertex_list[i], self.vertex_list[j], edge_weight))
                self.edge_set.append(Edge(self.vertex_list[j], self.vertex_list[i], edge_weight))
        pass
