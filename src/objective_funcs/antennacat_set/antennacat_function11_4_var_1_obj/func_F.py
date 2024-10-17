#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './antennacat_set/antennacat_function1/func_F.py'
#   objective function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: July 24, 2024
##-------------------------------------------------------------------------------\
import numpy as np

def func_F(X, NO_OF_OUTS=1):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        for i in range(NO_OF_OUTS):
            F[i] = 0.5 * np.sin(np.prod(X[:NO_OF_OUTS-i-1])+ X[0]**3)  + np.sin(X[0]**2) 
      
    except Exception as e:
        print(e)
        noErrors = False
    return F, noErrors