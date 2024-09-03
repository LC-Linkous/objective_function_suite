#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './multi_objective/ctp1_2_vars/constr_F.py'
#   constraints function for function compatable with project optimizers.
#   Includes extra error checking and recovery.
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 28, 2024
##-------------------------------------------------------------------------------\


import numpy as np

def constr_F(X):
    F = True

    return F