#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/test_function_4/configs_F.py'
#   configurations for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 25, 2024
##-------------------------------------------------------------------------------\

import sys
try: # for outside func calls
    sys.path.insert(0, './optimizer-benchmarking/src/objective_funcs/multi_objective/')
    from objective_funcs.multi_objective.test_function_4.func_F import func_F
    from objective_funcs.multi_objective.test_function_4.constr_F import constr_F
except: # for local
    from func_F import func_F
    from constr_F import constr_F

OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "test_function_4.func_F"
CONSTR_FUNC_NAME = "test_function_4.constr_F"

# problem dependent variables
LB = [[-7, -7]]         # Lower boundaries
UB = [[4, 4]]           # Upper boundaries
IN_VARS = 2             # Number of input variables (x-values)
OUT_VARS = 2            # Number of output variables (y-values)
TARGETS = [12.0, -7.0]  # Target values for output, on pareto front
GLOBAL_MIN = None       # Global minima, if they exist
