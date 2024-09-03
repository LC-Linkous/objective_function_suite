#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective_single_input/one_input_griewank/func_F.py'
#   objective function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 28, 2024
##-------------------------------------------------------------------------------\

import numpy as np

def func_F(X, NO_OF_OUTS=1):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        x = X[0]
        term1 = x**2 / 4000
        term2 = np.cos(x / np.sqrt(1))
        F = term1 - term2 + 1
    except:
        noErrors = False

    return [F], noErrors
