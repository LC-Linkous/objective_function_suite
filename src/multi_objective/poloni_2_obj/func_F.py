#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/poloni_2_obj/func_F.py'
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

        A1 = 0.5*np.sin(1) - 2*np.cos(1) + np.sin(2) - 1.5*np.cos(2)
        A2 = 1.5*np.sin(1) - 1*np.cos(1) + 2*np.sin(2) - 0.5*np.cos(2)
        B1 = 0.5*np.sin(x1) - 2*np.cos(x1) + np.sin(x2) - 1.5*np.cos(x2)
        B2 = 1.5*np.sin(x1) - 1*np.cos(x1) + 2*np.sin(x2) - 0.5*np.cos(x2)
        F[0] = 1 + (A1-B1)**2 + (A2-B2)**2
        F[1] = (x1 + 3)**2 + (x2 + 1)**2

    except:
        noErrors = False
    
    return F, noErrors
