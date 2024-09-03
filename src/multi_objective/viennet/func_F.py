#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/viennet/func_F.py'
#   objective function for function compatable with project optimizers
#   Includes additional error checking and handling for under/overflow.
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 30, 2024
##-------------------------------------------------------------------------------\

import numpy as np

def func_F(X, NO_OF_OUTS=3):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        x1, x2 = X[0], X[1]

        F[0] = 0.5*(x1**2 + x2**2) + np.sin(x1**2+x2**2)
        F[1] = (((3*x1-2*x2+4)**2)/8) + (((x1-x2+1)**2)/27) + 15
        F[2] = 1/(x1**2+x2**2+1) - 1.1*np.exp(-(x1**2 + x2**2))
    except:
        noErrors = False
    
    return F, noErrors
