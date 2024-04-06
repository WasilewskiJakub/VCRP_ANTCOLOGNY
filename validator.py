from Graph import *

class SolutionValidator:
    def __init__(self,graph) -> None:
        self.graph = graph
        pass
    
    def rateSolution(self,solution):
        overallSum = 0
        for route in solution:
            for i in range(len(route)-1):
                overallSum += self.graph.edges[route[i]][route[i+1]]
        return overallSum
    
    def checkIfAllVertexVisited(self,solution):
        visited = [False] * self.graph.size
        for route in solution[1]:
            for v in route:
                visited[v] = True
        return not (False in visited)         
    
    def validateSollution(self, solution):
        print("Total length of trace is: ",solution[0])
        for i,route in enumerate(solution[1]):
            print(i+1,".",route, " Length: ",self.rateSolution([route]))
        print("All custommers visited: ","\033[92mTrue\033[0m" if self.checkIfAllVertexVisited(solution) else "\033[91mFalse\033[0m" )
