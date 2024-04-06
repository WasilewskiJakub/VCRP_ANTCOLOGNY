import numpy as np
from Graph import *
from validator import SolutionValidator

class CVRP_Brutal:
    def __init__(self,graph:Graph)->None:
        self.graph = graph
        self.solutionValidator = SolutionValidator(self.graph)
        pass

    def findSolution(self, maxCapacity:int):
        visited = [False] * len(self.graph.vertex)
        magazine_idx = 0
        visited[magazine_idx] = True
        solution = list()
        while False in visited:
            route = list()
            current_customer = magazine_idx
            route.append(current_customer)
            capacity = maxCapacity
            while(False in visited):    
                unvisited = np.where(np.logical_not(visited))[0]
                neighbors = self.graph.neighbors(current_customer)
                minDistance = float("inf")
                next_customer = None
                for vertex in unvisited:
                    if vertex in neighbors: 
                        distToNeighbour = self.graph.edges[current_customer][vertex]
                        if minDistance > distToNeighbour:
                            minDistance = distToNeighbour
                            next_customer = vertex 

                
                capacity -= self.graph.edges[current_customer][next_customer]
                # truck must have enough capacity to deliver order to client
                if(capacity > 0):
                    route.append(next_customer)
                    visited[next_customer] = True
                else:
                    break
            route.append(magazine_idx) # back to magazine
            solution.append(route)
        return (self.solutionValidator.rateSolution(solution), solution)
    def validateSollution(self, solution):
        self.solutionValidator.validateSollution(solution) 