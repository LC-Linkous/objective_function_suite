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

def func_F(X, NO_OF_OUTS=2):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        for i in range(NO_OF_OUTS-1):
            F[i] = np.sin(np.prod(X[:NO_OF_OUTS-i-1]))  +  np.cos(X[0]**3)
        F[NO_OF_OUTS-1] = (1 - X[0]) 

    except Exception as e:
        print(e)
        noErrors = False
    return F, noErrors