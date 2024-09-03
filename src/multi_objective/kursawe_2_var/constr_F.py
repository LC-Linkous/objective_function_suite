#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/kursawe_2_var/constr_F.py'
#   constraints function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: March 31, 2024
##-------------------------------------------------------------------------------\


import numpy as np

def constr_F(X):
    F = True
    if (isinstance(X, list)) or (isinstance(X, np.ndarray)):
        if (len(X) < 1) or (len(X)>3):
            F = False
            return F

        for el_x in X:
            if (el_x <-5) or (5 < el_x):
                F = False
                return F
    else: #int, float, etc
        if (X <-5) or (5 < X):
            F = False
            return F
    
    return F
