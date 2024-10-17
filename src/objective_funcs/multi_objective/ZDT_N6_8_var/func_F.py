#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/ZDT_N6_8_var/func_F.py'
#   objective function for function compatable with project optimizers
#   Additional error checking and handle has been added.
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
            n = len(X)
            if n == 1:
                g = 1
            else:
                #NOTE: numpy as off 5/24 does not allow raising negative numbers to 
                # factional powers, even if it does not cause a complex number.
                #g = 1 + 9*(sum(X[1:])/(n-1))**(0.25) <- throws error with power
                a = sum(X[1:])/(n-1)
                expTerm = np.sign(a) * (np.abs(a)) ** (1 / 4)
                g = 1 + 9*expTerm
            # additional constraints added to handle np.exp() and **2 under/overflows
            F[0] = 1-np.exp(-4*X[0])*np.sin(6*np.pi*X[0])**6
            h = 1 - (F[0]/g)**2 
            F[1] = g*h
        else: # single val, not array
            F[0] = 1-np.exp(-4*X)*np.sin(6*np.pi*X)**6
            g = 1 # 9*(sum(X[1:9])/(n-1))**(0.25) <- this includes vals that the single var version doesnt have
            h =  1 - (F[0]/g)**2 
            F[1] = g*h


    except:
        noErrors = False
    
    return F, noErrors
