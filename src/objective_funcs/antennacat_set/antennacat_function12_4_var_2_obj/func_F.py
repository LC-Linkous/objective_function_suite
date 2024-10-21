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
            if i < M - 1:
                F[i] = sum(np.cos((np.pi * x_j) / 2) for x_j in X) + np.sin((np.pi * X[i]) / 2)
            else:
                F[i] = np.sin((np.pi * X[M - 1]) / 2)

    except Exception as e:
        print(e)
        noErrors = False
    return F, noErrors
