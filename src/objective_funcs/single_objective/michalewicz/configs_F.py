#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective/michalewicz/configs_F.py'
#   configurations for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 25, 2024
##-------------------------------------------------------------------------------\


import sys
try: # for outside func calls
    sys.path.insert(0, './src/objective_funcs/single_objective/')
    from single_objective.michalewicz.func_F import func_F
    from single_objective.michalewicz.constr_F import constr_F
except: # for local
    from func_F import func_F
    from constr_F import constr_F

import numpy as np

OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "michalewicz.func_F"
CONSTR_FUNC_NAME = "michalewicz.constr_F"

# problem dependent variables
LB = [[0, 0]]             # Lower boundaries
UB = [[np.pi, np.pi]]               # Upper boundaries
IN_VARS = 2                 # Number of input variables (x-values)
OUT_VARS = 1                # Number of output variables (y-values) 
TARGETS = [-1.8013]         # Target values for output
GLOBAL_MIN = [[2.2, 1.57]]  # Global minima, if they exist 

# has d local minima.
# 2 dimensional: f(2.2, 1.57) = -1.8013
# 5 dimensional: f(x_5) = -4.688
# 10 dimensional: f(x_10) = -9.660