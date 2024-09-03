#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective/branin/func_F.py'
#   objective function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 28, 2024
##-------------------------------------------------------------------------------\

# https://www.sfu.ca/~ssurjano/branin.html

import numpy as np

def func_F(X, a=1, b=5.1/(4*np.pi**2),c=(5/np.pi), r=6, s=10, t=1/(8*np.pi), NO_OF_OUTS=1):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        x = X[0]
        y = X[1]   
        F = a*(y-b*(x**2)+c*x-r)**2 + s*(1-t)*np.cos(x)+1
    except:
        noErrors = False

    return [F], noErrors
