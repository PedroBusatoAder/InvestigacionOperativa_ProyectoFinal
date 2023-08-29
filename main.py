import picos

from scipy import optimize
from scipy.spatial.distance import cdist

import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

from geoPositions import *


def firsOptimizaition():
    P = picos.Problem()

    #Decisiones variables --> It is working with integer values but not real ones
    hurti = picos.IntegerVariable('h', 11, lower = 0)                                                               #Amount of Hurtigladere chargers to be installed in each of the provincies
    lyn = picos.IntegerVariable('l', 11, lower = 0)                                                                 #Amount of Lynladere chargers to be installed in each of the provincies

    #Costs associated to variables
    costHurti = np.array([45000, 45000, 45000, 45000, 45000, 45000, 45000, 45000, 45000, 45000, 45000])             #Cost matrix for the Hurtigladere chargers in each of the provincies
    costLyn = np.array([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])
    
    #Optimization function
    P.set_objective('min', costHurti.T * hurti + costLyn.T * lyn)

    #Demand constains   
    demandByProvince = np.array([2144636, 1702321, 1651337, 1152372, 8296265, 4082799, 848626, 3505345, 3029488, 6066878, 12176541])
    demandByProvince = np.array([2144635, 1702320, 1651340, 1152370, 8296265, 4082800, 848625, 3505345, 3029490, 6066880, 12176540])/5
    
    for i in range(len(demandByProvince)):
        demandGenerated = np.random.normal(loc = 14.5, scale = 1.5)                                         #Suppose that demand comes from a Normal distribution
        P.add_constraint(hurti[i]*(90.5) + lyn[i]*(300) == demandByProvince[i])

    print(P)
    P.solve()

    # Representing our outputs in a table for a clearer undestanding
    table_data = []
    for i in range(11):
        table_data.append([hurti.value[i], lyn.value[i]])

    # Defining the table headers
    headers = ['Hurtigladere', 'Lynladere']

    # Printing the table
    print(tabulate(table_data, headers = headers, floatfmt=".0f"))

    return(hurti, lyn)

def secondOptimization(amountOfStations):
    P = picos.Problem()
    
    x = picos.BinaryVariable('x', 15)                                       # We build or not in this particular district in Oslo
    s = picos.IntegerVariable(s, amountOfStations, lower = 0)               # Amount of physical construction places we need for setting up the stations 

    P.set_objective('min', sum(x*s))
    
    P.solve()
    print(x)




# def secondOptimization(totalStations):
#     print("Total estaciones", totalStations)

#     munis = np.array([[10,20], [56,12], [78,0]])

#     def objectiveFunction(x, munis):
#         stations = x.reshape((totalStations,2))
#         distances = cdist(munis, stations, 'euclidean')
#         return np.sum(distances)

#     def constrain1(x):
#         stations = x.reshape((totalStations,2))
#         distances = cdist(x,x, "euclidean")
#         for i in range(totalStations):
#             for j in range(i+1, totalStations):
#                     res2 = optimize.NonlinearConstraint(fun = r2, lb = 60 * 1000000, ub = np.inf)

#     seed = np.zeros(2 * totalStations)

#     # limits = [(),()]                                                                 # Geographical limits for each of our provinces --> Bounds
#     optimal = optimize.minimize(fun = objectiveFunction, args=(munis,), x0 = seed)
#     print(optimal)
#     if(optimal.success):
#         print(optimal.x)

def main():
    optimalHurti, optimalLyn = firsOptimizaition()                                   #We save our optimal amount of charging stations, from where we will decide how to place them on the map
    
    for i in range(11):
        totalStations = optimalHurti[i] + optimalLyn[i]
        secondOptimization(4)


main()


#Identificar por provincia una cierta cantidad de ciudades donde colocar --> Cada ciudad es una binaria
#