#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective_single_input/one_input_rosenbrock/func_F.py'
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
        F = (1-x)**2 + 100*(x-1)**2
    except:
        noErrors = False

    return [F], noErrors
