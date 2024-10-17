#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './multi_objective/ctp1_2_vars/configs_F.py'
#   configurations for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 25, 2024
##-------------------------------------------------------------------------------\

import sys
try:
    sys.path.insert(0, './src/objective_funcs/multi_objective/')
    from multi_objective.ctp1_2_vars.func_F import func_F
    from multi_objective.ctp1_2_vars.constr_F import constr_F
except:
    from func_F import func_F
    from constr_F import constr_F

OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "ctp1_2_vars.func_F"
CONSTR_FUNC_NAME = "ctp1_2_vars.constr_F"

# problem dependent variables
LB = [[0, 0]]       # Lower boundaries for input
UB = [[1, 1]]       # Upper boundaries for input
IN_VARS = 2         # Number of input variables (x-values)
OUT_VARS = 2        # Number of output variables (y-values) 
TARGETS = [0.0, 1.0]    # Target values for output, on pareto front
GLOBAL_MIN = None   # Global minima, if they exist
