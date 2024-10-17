#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective/beale/configs_F.py'
#   configurations for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 25, 2024
##-------------------------------------------------------------------------------\


import sys
try: # for outside func calls
    sys.path.insert(0, './src/objective_funcs/single_objective/')
    from single_objective.beale.func_F import func_F
    from single_objective.beale.constr_F import constr_F
except: # for local
    from func_F import func_F
    from constr_F import constr_F


OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "beale.func_F"
CONSTR_FUNC_NAME = "beale.constr_F"

# problem dependent variables
LB = [[-4.5, -4.5]]         # Lower boundaries
UB = [[4.5, 4.5]]           # Upper boundaries
IN_VARS = 2                 # Number of input variables (x-values)
OUT_VARS = 1                # Number of output variables (y-values) 
TARGETS = [0]               # Target values for output
GLOBAL_MIN = [[3, 0.5]]     # Global minima, if they exist 
