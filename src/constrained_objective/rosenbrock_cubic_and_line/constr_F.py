#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './constrained_objective/rosenbrock_cubic_and_line/constr_F.py'
#   constraints function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: March 31, 2024
##-------------------------------------------------------------------------------\


import numpy as np

def constr_F(X):
    # returns F = True if the (X[0], X[1]) pair is within the constraints. Otherwise returns False.
    F = True #default
    # check cubic condition
    cubic = (X[0]-1)**3 - X[1] + 1
    if cubic > 0:
        F = False
        return F

    # check line condition
    line = X[0]+X[1]-2
    F = (line <= 0)
    return F