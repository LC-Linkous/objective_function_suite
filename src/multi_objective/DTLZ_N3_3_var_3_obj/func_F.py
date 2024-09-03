#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/DTLZ_N3_3_var_3_obj/func_F.py'
#   objective function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 28, 2024
##-------------------------------------------------------------------------------\

import numpy as np

def func_F(X, NO_OF_OUTS=3):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        
        g_value = 100 * (len((X[NO_OF_OUTS-1:])) + np.sum(((X[NO_OF_OUTS-1:]) - 0.5)**2 - np.cos(20 * np.pi * ((X[NO_OF_OUTS-1:]) - 0.5))))
        
        for i in range(NO_OF_OUTS-1):
            product = np.prod(X[:NO_OF_OUTS-i-1])
            F[i] = (1 + g_value) * np.cos(X[:NO_OF_OUTS-i-1] * np.pi / 2).prod()
        F[NO_OF_OUTS-1] = (1 + g_value) * np.sin(X[0] * np.pi / 2) * product

    except Exception as e:
        print(e)
        noErrors = False
    return F, noErrors
