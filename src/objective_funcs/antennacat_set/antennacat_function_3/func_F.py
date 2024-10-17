#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './antennacat_set/antennacat_function1/func_F.py'
#   objective function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 28, 2024
##-------------------------------------------------------------------------------\

import numpy as np
import time

def func_F(X, NO_OF_OUTS=1):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        x = X[0]
        if x < 0:
            F = 1
        elif x == 0:
            F = 0
        elif x <= .25:
            F = .5
        elif x <= .3:
            F = 1
        elif x <= .4:
            F = 1.25
        elif x <= .5:
            F = 1.5
        elif x <= .75:
            F = 2
        else:
            F = 3
    except:
        noErrors = False

    return [F], noErrors
