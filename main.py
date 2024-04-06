from Graph import *
import numpy as np
import random
from ACO import *
from brutal import *
import time

print("Ant Cologny Algorithm")
g = Graph(25)
ACO = AntColognyySolver(g)
BRUTAL = CVRP_Brutal(g)
solver = SolutionValidator(g)
print("Brutal:")
start_time = time.time()
solver.validateSollution(BRUTAL.findSolution(100))
elapsed_time = time.time() - start_time
print("Time:", elapsed_time, "s")

print("ACO SIMPLE:")
start_time = time.time()
solver.validateSollution(ACO.Simple(28,30,100,0.8,0.3,5))
elapsed_time = time.time() - start_time
print("Time:", elapsed_time, "s")

print("ACO ELITIST:")
start_time = time.time()
solver.validateSollution(ACO.Elitist(28,30,100,0.8,0.3,5))
elapsed_time = time.time() - start_time
print("Time:", elapsed_time, "s")

print("ACO MAX-MIN:")
start_time = time.time()
solver.validateSollution(ACO.MaxMin(28,30,100,0.8,0.3,5))
elapsed_time = time.time() - start_time
print("Time:", elapsed_time, "s")

