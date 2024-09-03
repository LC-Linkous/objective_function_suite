#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/schaffer_N2/func_F.py'
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
        if X<=1:
            F[0] = -X
        elif 1<X<=3:
            F[0] = X-2
        elif 3<X<=4:
            F[0] = 4-X
        else: # x>4:
            F[0] = X-4    

        F[1] = (X - 5)**2

    except:
        noErrors = False
    
    return F, noErrors
