#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/ZDT_N1_2_var/constr_F.py'
#   constraints function for function compatable with project optimizers
#   Additional error checking and handle has been added.
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 20, 2024
##-------------------------------------------------------------------------------\


import numpy as np

def constr_F(X):
    F = True
    if (isinstance(X, list)) or (isinstance(X, np.ndarray)):
        if (len(X) < 1) or (len(X)>30):
            F = False
    #     # check for values that cause complex vals with the square root (rare, but does happen)
    #     n = len(X)
    #     if n == 1:
    #         g = 1
    #     else:
    #         g = 1 + (9/(n-1))*sum(X[1:])
    #     if (X[0]/g) <= 0: #negative 
    #         # this causes a complex in the objective function (func_F) with the np.sqrt() call
    #         F = False
        
    # else:  #int, float, etc
    #     F = True
    return F