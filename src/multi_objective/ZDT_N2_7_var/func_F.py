#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/ZDT_N2_7_var/func_F.py'
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
        if (isinstance(X, list)) or (isinstance(X, np.ndarray)):
            n = len(X)
            if n == 1:
                g = 1
            else:
                g = 1 + (9/(n-1))*sum(X[1:])
            F[0] = X[0]
            h = 1 -  (F[0]/g)**2
            F[1] = g*h
        else: # single val, not array
            F[0] = X
            g = 1 #+ (9/29)*sum(X[1:])<- this x is x_2, whic doesnt exist for single var
            h = 1 -  (F[0]/g)**2
            F[1] = g*h

    except:
        noErrors = False
    
    return F, noErrors