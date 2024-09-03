#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './multi_objective/chankong_haimes/configs_F.py'
#   configurations for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 25, 2024
##-------------------------------------------------------------------------------\


import sys
try:
    sys.path.insert(0, './objective_funcs/multi_objective/')
    from multi_objective.chankong_haimes.func_F import func_F
    from multi_objective.chankong_haimes.constr_F import constr_F
except:
    from func_F import func_F
    from constr_F import constr_F

OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "chankong_haimes.func_F"
CONSTR_FUNC_NAME = "chankong_haimes.constr_F"

# problem dependent variables
LB = [[-20, -20]]                 # Lower boundaries for input
UB = [[20, 20]]                   # Upper boundaries for input
IN_VARS = 2                       # Number of input variables (x-values)
OUT_VARS = 2                      # Number of output variables (y-values) 
TARGETS = [10.3996531,4.67084991] # Target values for output, on pareto front
#TARGETS = [70, 0]                # Target values for output, in objective space
GLOBAL_MIN = None                 # Global minima, if they exist
