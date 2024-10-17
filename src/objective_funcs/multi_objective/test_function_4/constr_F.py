#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/test_function_4/constr_F.py'
#   constraints function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: March 31, 2024
##-------------------------------------------------------------------------------\


import numpy as np

def constr_F(X):
    x1, x2 = X[0], X[1]

    F = True

    if ((6.5 - x1/6 - x2) < 0) or ((7.5-0.5*x1 - x2) < 0) or ((30-5*x1-x2) < 0):
        F = False

    return F