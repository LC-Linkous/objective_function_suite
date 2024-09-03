#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective/cross_in_tray/func_F.py'
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
        term1 = np.sin(x) * np.sin(y)
        term2 = np.exp(np.abs(100 - np.sqrt(x**2 + y**2) / np.pi))
        F = -0.0001 * (np.abs(term1 * term2) + 1)**0.1
    except:
        noErrors = False

    return [F], noErrors
