#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/DTLZ_N1_10_var_5_obj/func_F.py'
#   objective function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: July 24, 2024
##-------------------------------------------------------------------------------\

import numpy as np

def func_F(X, NO_OF_OUTS=5):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        g = np.sum((X[NO_OF_OUTS-1:] - 0.5)**2 - np.cos(20 * np.pi * (X[NO_OF_OUTS-1:] - 0.5)), axis=0)
        # g calculates, so reset F
        F = np.empty(NO_OF_OUTS)
        for i in range(NO_OF_OUTS):
            F [i] = 0.5 * (1 + g)
            for j in range(NO_OF_OUTS - 1 - i):
                F [i] *= X[j]
            if i > 0:
                F [i] *= (1 - X[NO_OF_OUTS - 1 - i])

    except Exception as e:
        print(e)
        noErrors = False
    return F, noErrors
