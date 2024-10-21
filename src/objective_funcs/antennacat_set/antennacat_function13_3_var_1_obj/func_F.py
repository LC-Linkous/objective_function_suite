#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './antennacat_set/antennacat_function1/func_F.py'
#   objective function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: July 24, 2024
##-------------------------------------------------------------------------------\
import numpy as np

def func_F(X, NO_OF_OUTS=1):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        M = len(X)
        for i in range(NO_OF_OUTS):
            sum_value = sum(np.cos((i * np.pi * x_j) / M) + np.sin((i * np.pi * x_j) / M) for x_j in X)
            F[i] = (1 / M) * sum_value

    except Exception as e:
        print(e)
        noErrors = False
    return F, noErrors