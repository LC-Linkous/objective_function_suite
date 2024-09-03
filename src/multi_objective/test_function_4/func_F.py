#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/test_function_4/func_F.py'
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
        x1, x2 = X[0], X[1]

        F[0] = x1**2 - x2
        F[1] = -0.5*x1 - x2 -1

    except:
        noErrors = False
    
    return F, noErrors
