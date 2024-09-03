#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './single_objective_single_input/one_input_griewank/configs_F.py'
#   configurations for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 25, 2024
##-------------------------------------------------------------------------------\


import sys

try: # for outside func calls
    sys.path.insert(0, './src/single_objective_single_input/')
    from single_objective_single_input.one_input_griewank.func_F import func_F
    from single_objective_single_input.one_input_griewank.constr_F import constr_F
except: # for local
    from func_F import func_F
    from constr_F import constr_F

OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "one_input_griewank.func_F"
CONSTR_FUNC_NAME = "one_input_griewank.constr_F"

# problem dependent variables
LB = [[0]]                  # Lower boundaries
UB = [[1]]                  # Upper boundaries
IN_VARS = 1                 # Number of input variables (x-values)
OUT_VARS = 1                # Number of output variables (y-values) 
TARGETS = [0]               # Target values for output
GLOBAL_MIN = [[0]]       # Global minima sample, if they exist. 