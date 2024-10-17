#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './multi_objective/binh_korn/constr_F.py'
#   constraints function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 28, 2024
##-------------------------------------------------------------------------------\


import numpy as np

def constr_F(x):
    F = True
    if (((x[0]-5)**2 + x[1]**2) > 25) or (((x[0]-8)**2+(x[1]+3)**2) <7.7):
        F = False

    return F