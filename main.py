from Graph import *
import numpy as np
import random
from ACO import *
from brutal import *

print("Ant Cologny Algorithm")
g = Graph(22)
ACO = AntColognyySolver(g)
solver = SolutionValidator(g)
#g.printGraph()
solver.validateSollution(ACO.Simple(18,30,40,0.8,0,12))
brutal = CVRP_Brutal(g)
solver.validateSollution(brutal.findSolution(40))


