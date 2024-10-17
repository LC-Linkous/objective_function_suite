#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './multi_objective/constr_ex_problem/constr_F.py'
#   constraints function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 20, 2024
##-------------------------------------------------------------------------------\


import numpy as np

def constr_F(X):
    x1, x2 = X[0], X[1]
    F = True

    if ((x2+9*x1)<6) or ((-x2+9*x1)<1):
        F = False
    return F