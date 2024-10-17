#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective/ackley/func_F.py'
#   objective function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 28, 2024
##-------------------------------------------------------------------------------\

import numpy as np

def func_F(X, a=20, b=0.2, c=2 * np.pi, NO_OF_OUTS=1):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        x = X[0]
        y = X[1]
        term1 = -a * np.exp(-b *np.sqrt((x**2 + y**2) / 2))
        term2 = -np.exp((np.cos(c * x) + np.cos(c * y)) / 2)
        F = term1 + term2 + a + np.exp(1)

    except:
        noErrors = False

    return [F], noErrors
