import picos
import numpy as np
import matplotlib.pyplot as plt

def main():
    P = picos.Problem()

    #Decisiones variables
    hurti = picos.IntegerVariable('h', 11, lower = 0)                                                           #Amount of Hurtigladere chargers to be installed in each of the provincies
    lyn = picos.IntegerVariable('l', 11, lower = 0)                                                             #Amount of Lynladere chargers to be installed in each of the provincies

    #Costs associated to variables
    costHurti = np.array([45000, 45000, 45000, 45000, 45000, 45000, 45000, 45000, 45000, 45000, 45000])         #Cost matrix for the Hurtigladere chargers in each of the provincies
    costLyn = np.array([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])
    
    #Optimization function
    P.set_objective('min', costHurti.T * hurti + costLyn.T * lyn)

    #Problem constains   
    demandByProvince = np.array([2144636, 1702321, 1651337, 1152372, 8296265, 4082799, 848626, 3505345, 3029488, 6066878, 12176541])

    for i in range(len(demandByProvince)):
        P.add_constraint( (hurti[i]*96.5 + lyn[i]*250) == demandByProvince[i])

    P.solve()

    print(hurti)
    print(lyn)
main()
