#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective/schaffer_N4/func_F.py'
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
        numerator = np.cos(np.sin(np.abs(x**2 - y**2)))**2 - 0.5
        denominator = (1 + 0.001 * (x**2 + y**2))**2
        F = 0.5 + numerator / denominator

    except:
        noErrors = False

    return [F], noErrors
