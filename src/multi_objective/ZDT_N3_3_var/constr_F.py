#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/ZDT_N3_3_var/constr_F.py'
#   constraints function for function compatable with project optimizers
#   Additional error checking and handle has been added.
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 18, 2024
##-------------------------------------------------------------------------------\


import numpy as np

def constr_F(X):
    F = True
    if (isinstance(X, list)) or (isinstance(X, np.ndarray)):
        if (len(X) < 1) or (len(X)>30):
            F = False
    return F