#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/DTLZ_N2_3_var_3_obj/func_F.py'
#   objective function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 28, 2024
##-------------------------------------------------------------------------------\

import numpy as np

def func_F(X, NO_OF_OUTS=4):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:

       
        g_value = np.sum(((X[NO_OF_OUTS-1:]) - 0.5)**2)
        
        cos_terms = np.cos(X[:NO_OF_OUTS-1] * np.pi / 2)
        sin_term = np.sin(X[:NO_OF_OUTS-2] * np.pi / 2)
        cos_product = np.prod(cos_terms)
        
        for i in range(NO_OF_OUTS-1):
            F[i] = (1 + g_value) * cos_product
            F[i] *= cos_terms[i]
        
        F[NO_OF_OUTS-1] = (1 + g_value) * cos_product
        F[NO_OF_OUTS-1] *= sin_term[-1]


    except Exception as e:
        print(e)
        noErrors = False
    return F, noErrors
