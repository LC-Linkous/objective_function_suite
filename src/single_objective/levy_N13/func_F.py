#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective/levy_N13/func_F.py'
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
        F = (np.sin(3 * np.pi * x)**2 
                + (x - 1)**2 * (1 + np.sin(3 * np.pi * y)**2) 
                + (y - 1)**2 * (1 + np.sin(2 * np.pi * y)**2))
  
    except:
        noErrors = False

    return [F], noErrors
  