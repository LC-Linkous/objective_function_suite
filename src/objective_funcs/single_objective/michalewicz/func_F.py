#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective/michalewicz/func_F.py'
#   objective function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 28, 2024
##-------------------------------------------------------------------------------\

import numpy as np

def func_F(X, m=10, NO_OF_OUTS=1):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        d = len(X)
        F =  -sum(np.sin(X[i]) * np.sin((i + 1) * X[i]**2 / np.pi)**(2 * m) for i in range(d))
   
    except:
        noErrors = False

    return [F], noErrors
