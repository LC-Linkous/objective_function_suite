#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/osyczka_kundu_6_vars/constr_F.py'
#   constraints function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: March 31, 2024
##-------------------------------------------------------------------------------\


import numpy as np

def constr_F(X):
    F = True
    x1, x2, x3, x4, x5, x6 = X[0], X[1], X[2], X[3], X[4], X[5]
    term1 = x1 + x2 -2
    term2 = 6 - x1 - x2
    term3 = 2 - x2 + x1
    term4 = 2 - x1 + 3*x2
    term5 = 4 - (x3-3)**2 - x4
    term6 = (x5 - 3)**2 + x6 - 4

    if (term1<0) or (term2<0) or (term3<0) or (term4<0) or (term5<0) or (term6<0):
        F = False
    return F