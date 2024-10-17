#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/ZDT_N4_7_var/constr_F.py'
#   constraints function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 18, 2024
##-------------------------------------------------------------------------------\

import numpy as np

def constr_F(X):
    F = True
    if (isinstance(X, list)) or (isinstance(X, np.ndarray)):
        if (len(X) < 2) or (len(X)>10):
            F = False
            return F
        if (X[0]<0) or (X[0]>1):
            F = False
            return F
        F = all((-5<=x<=5) for x in X[1:]) #gets True if x in range -5 to 5
    else:
        F = False # this function requires at least 2 elements
    return F