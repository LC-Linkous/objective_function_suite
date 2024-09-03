#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/kursawe_gen/constr_F.py'
#   constraints function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: April 4, 2024
##-------------------------------------------------------------------------------\


import numpy as np

def constr_F(X):
    F = True
    if (len(X) < 1):# or (len(X)>3): #removing the upper limit for the general function
        F = False
        return F

    for el_x in X:
        if (el_x <-5) or (5 < el_x):
            F = False
            return F
    return F