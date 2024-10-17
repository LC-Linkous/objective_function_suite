#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/ZDT_N4_6_var/func_F.py'
#   objective function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 28, 2024
##-------------------------------------------------------------------------------\

import numpy as np

def func_F(X, NO_OF_OUTS=2):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        if (isinstance(X, list)) or (isinstance(X, np.ndarray)):
            n = len(X)
            g = 1 + 10*(n-1) + sum((X[1:]**2)-10*np.cos(4*np.pi*X[1:]))
            F[0] = X[0]
            h = 1 - np.sqrt(F[0]/g)
            F[1] = g*h
        else:
            noErrors = False # this function requires at least 2 elements

    except:
        noErrors = False
    
    return F, noErrors
