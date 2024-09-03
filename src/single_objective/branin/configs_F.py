#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective/branin/configs_F.py'
#   configurations for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 25, 2024
##-------------------------------------------------------------------------------\


import sys
try: # for outside func calls
    sys.path.insert(0, './src/objective_funcs/single_objective/')
    from single_objective.branin.func_F import func_F
    from single_objective.branin.constr_F import constr_F
except: # for local
    from func_F import func_F
    from constr_F import constr_F

import numpy as np

OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "branin.func_F"
CONSTR_FUNC_NAME = "branin.constr_F"

# problem dependent variables
LB = [[-5, 0]]         # Lower boundaries
UB = [[10, 15]]        # Upper boundaries
IN_VARS = 2            # Number of input variables (x-values)
OUT_VARS = 1           # Number of output variables (y-values) 
TARGETS = [0.397887]   # Target values for output
                       # Global minima, if they exist
GLOBAL_MIN = [[-np.pi, 12.275], 
              [np.pi, 2.275],
              [9.42479, 2.475]]  
