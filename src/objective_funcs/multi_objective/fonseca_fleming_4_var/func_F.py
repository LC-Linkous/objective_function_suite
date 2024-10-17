#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/fonseca_fleming_4_var/func_F.py'
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
        n = np.size(X)

        term1 = np.exp(-np.sum((X - 1/np.sqrt(n))**2))
        term2 = np.exp(-np.sum((X + 1/np.sqrt(n))**2))

        F[0] = 1 - term1
        F[1] = 1 - term2
    except:
        noErrors = False

    return F, noErrors

