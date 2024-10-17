#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective/beale/func_F.py'
#   objective function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 28, 2024
##-------------------------------------------------------------------------------\

import numpy as np

def func_F(X, NO_OF_OUTS=1):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        x = X[0]
        y = X[1]   
        term1 = (1.5 - x + x * y) ** 2
        term2 = (2.25 - x + x * y ** 2) ** 2
        term3 = (2.625 - x + x * y ** 3) ** 2
        F = term1 + term2 + term3
    except:
        noErrors = False

    return [F], noErrors
