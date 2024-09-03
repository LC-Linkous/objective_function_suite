#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/kursawe_3_var/func_F.py'
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
            F[0] = np.sum(-10 * np.exp(-0.2 * np.sqrt(X[:-1]**2 + X[1:]**2)))
            F[1] = np.sum(np.abs(X)**0.8 + 5 * np.sin(X**3))
        else: #single input
            F[0] = np.sum(-10 * np.exp(-0.2 * np.sqrt(X**2)))
            F[1] = np.sum(np.abs(X)**0.8 + 5 * np.sin(X**3))  

    except:
        noErrors = False
    
    return F, noErrors
