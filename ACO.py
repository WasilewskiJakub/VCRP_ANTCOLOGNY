import numpy as np
from Graph import *
from validator import SolutionValidator

class AntColognyySolver:
    
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.solutionValidator = SolutionValidator(self.graph)
        pass
    
    def Simple(self, maxIter:int, maxPathLength:int, maxCapacity:int, alpha:float, beta:float, antsQ:int)->None:
        n = self.graph.size
        self.alpha = alpha
        self.beta = beta
        self.maxPathLength = maxPathLength
        self.maxCapacity = maxCapacity 
        self.pheromone = np.ones((n,n))
        #solutionList = []
        bestSollution = (float("inf"),None)
        for i in range(maxIter):
            antSollution = []
            for ant in range(antsQ):
                solution = self.ant_sollution()
                rate = self.solutionValidator.rateSolution(solution)
                if rate < bestSollution[0]:
                    bestSollution = (rate,solution)
                antSollution.append((rate,solution))
            for i in range(n):
                for j in range(n):
                    self.updatePheromone(i, j, antSollution)
            #solutionList += antSollution
        return bestSollution
    
    def ant_sollution(self):
        
        visited = [False] * len(self.graph.vertex)
        magazine_idx = 0
        visited[magazine_idx] = True
        solution = list()
        
        while False in visited:
            route = list()
            current_customer = magazine_idx
            route.append(current_customer)
            capacity = self.maxCapacity
            #unvisited = np.where(np.logical_not(visited))[0] #magazine station index
            #probabilities = np.zeros(len(unvisited))
            
            while(False in visited):
                
                unvisited = np.where(np.logical_not(visited))[0]
                probabilities = np.zeros(len(unvisited))
                
                # Set probabilities for unvisited customers
                for i,unvisitedPoint in enumerate(unvisited):
                    probabilities[i] = self.probabilities(current_customer, unvisitedPoint, unvisited)
                probabilities/=np.sum(probabilities)
                
                next_customer = np.random.choice(unvisited, p=probabilities)
                capacity -= self.graph.edges[current_customer][next_customer]

                # truck must have enough capacity to deliver order to client
                if(capacity > 0):
                    route.append(next_customer)
                    visited[next_customer] = True
                else:
                    break
            
            route.append(magazine_idx) # back to magazine
            solution.append(route)
        return solution
    
    def probabilities(self,current_customer:int, next_customer:int, all_neighbors):
        def calculatePhi(current_customer,next_customer):
            return self.pheromone[current_customer,next_customer]
        
        def calculateNi(current_customer,next_customer):
            return 1/(self.graph.edges[current_customer][next_customer])
        
        def calculateProb(phi,ni):
            return (phi**self.alpha) * (ni**self.beta)
        
        total_sum = sum(calculateProb(calculatePhi(current_customer,unvisitedPoint), calculateNi(current_customer,unvisitedPoint)) for unvisitedPoint in all_neighbors)
        return calculateProb(calculatePhi(current_customer,next_customer),calculateNi(current_customer,next_customer)) / total_sum
    
    def updatePheromone(self, current_customer, next_customer, solutions, min_pheromone = float("-inf"), max_pheromone = float("inf")):
        Q = 2 # jais tam wspolczynnik
        p = 0.4 # współczynnik parowania feromonu
        deltaX = 0
        for i, solution in enumerate(solutions):
            for i in range(len(solution)-1):
                if solution[1][i] == current_customer and solution[1][i+1] == next_customer:
                    deltaX+= Q/solution[0]
        newValue = (1-p) * self.pheromone[current_customer, next_customer] + deltaX
        
        if newValue < min_pheromone:
            newValue = min_pheromone
        if newValue > max_pheromone:
            newValue = max_pheromone
        
        self.pheromone[current_customer,next_customer] = newValue
    
    def validateSollution(self, solution):
        self.solutionValidator.validateSollution(solution)

    #### ELITIST: In every iteration pheromone on best Solution path is increased 
    def Elitist(self, maxIter:int, maxPathLength:int, maxCapacity:int, alpha:float, beta:float, antsQ:int)->None:
        n = self.graph.size
        self.alpha = alpha
        self.beta = beta
        self.maxPathLength = maxPathLength
        self.maxCapacity = maxCapacity 
        self.pheromone = np.ones((n,n))
        #solutionList = []
        bestSollution = (float("inf"),None)
        for i in range(maxIter):
            #antSollution = []
            for ant in range(antsQ):
                solution = self.ant_sollution()
                rate = self.solutionValidator.rateSolution(solution)
                if rate < bestSollution[0]:
                    bestSollution = (rate,solution)
                #antSollution.append((rate,solution))
            for i in range(n):
                for j in range(n):
                    self.updatePheromone(i, j, [bestSollution])
            #solutionList += antSollution
        return bestSollution
    
    #### MAX-MIN: In every iteration pheromone on best Solution path in iteration is increased 
    def MaxMin(self, maxIter:int, maxPathLength:int, maxCapacity:int, alpha:float, beta:float, antsQ:int)->None:
        max_pheromone = 2
        min_pheromone = 0.5
        n = self.graph.size
        self.alpha = alpha
        self.beta = beta
        self.maxPathLength = maxPathLength
        self.maxCapacity = maxCapacity 
        self.pheromone = np.ones((n,n))
        #solutionList = []
        bestSollution = (float("inf"),None)
        for i in range(maxIter):
            #antSollution = []
            localBestSollution = (float("inf"),None)
            for ant in range(antsQ):
                solution = self.ant_sollution()
                rate = self.solutionValidator.rateSolution(solution)
                if rate < localBestSollution[0]:
                    localBestSollution = (rate,solution)
                #antSollution.append((rate,solution))
            for i in range(n):
                for j in range(n):
                    self.updatePheromone(i, j, [localBestSollution], min_pheromone, max_pheromone)
            if localBestSollution[0] < bestSollution[0]:
                    bestSollution = localBestSollution
            #solutionList += antSollution
        return bestSollution
        
