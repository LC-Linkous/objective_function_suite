#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/DTLZ_N1_5_var_5_obj/func_F.py'
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

        g_value = 100 * (len(X[NO_OF_OUTS-1:]) + np.sum((X[NO_OF_OUTS-1:] - 0.5)**2 - np.cos(20 * np.pi * (X[NO_OF_OUTS-1:] - 0.5))))
        for i in range(NO_OF_OUTS-1):
            F[i] = 0.5 * np.prod(X[:NO_OF_OUTS-i-1]) * (1 + g_value)
        F[NO_OF_OUTS-1] = 0.5 * (1 - X[0]) * (1 + g_value)

    except Exception as e:
        print(e)
        noErrors = False
    return F, noErrors