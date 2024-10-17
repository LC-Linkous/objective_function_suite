#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective_single_input/one_input_ackley/func_F.py'
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
        term1 = -20.0 * np.exp(-0.2 * np.sqrt(np.abs(x)))
        term2 = -np.exp(np.cos(2 * np.pi * x))
        F = term1 + term2 + 20 + np.exp(1)
    except:
        noErrors = False

    return [F], noErrors
