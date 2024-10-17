#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/osyczka_kundu_6_vars/func_F.py'
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
        x1, x2, x3, x4, x5, x6 = X[0], X[1], X[2], X[3], X[4], X[5]

        F[0] = -25*(x1-2)**2-(x2-2)**2-(x3-1)**2-(x4-4)**2-(x5-1)**2
        F[1] = sum(xi**2 for xi in X)
    except:
        noErrors = False
    
    return F, noErrors

