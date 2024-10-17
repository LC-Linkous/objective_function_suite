#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective/eggholder/func_F.py'
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
        term1 = -(y + 47) * np.sin(np.sqrt(np.abs(y + x / 2 + 47)))
        term2 = -x * np.sin(np.sqrt(np.abs(x - (y + 47))))
        F = term1 + term2
    except:
        noErrors = False

    return [F], noErrors
