#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './multi_objective/chankong_haimes/constr_F.py'
#   constraints function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: March 31, 2024
##-------------------------------------------------------------------------------\


import numpy as np

def constr_F(X):
    x1, x2 = X[0], X[1]
    F = True
    if ((x1**2 + x2**2) > 225) or ((x1-3*x2+10) > 0):
        F = False

    return F