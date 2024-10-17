#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './constrained_objective/rosenbrock_disk/configs_F.py'
#   configurations for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 25, 2024
##-------------------------------------------------------------------------------\


import sys
try: # for outside func calls
    sys.path.insert(0, './src/objective_funcs/constrained_objective/')
    from constrained_objective.rosenbrock_disk.func_F import func_F
    from constrained_objective.rosenbrock_disk.constr_F import constr_F
except: # for local
    from func_F import func_F
    from constr_F import constr_F

OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "rosenbrock_disk.func_F"
CONSTR_FUNC_NAME = "rosenbrock_disk.constr_F"

# problem dependent variables
LB = [[-1.5, -1.5]]      # Lower boundaries for input
UB = [[1.5, 1.5]]        # Upper boundaries for input
IN_VARS = 2              # Number of input variables (x-values)
OUT_VARS = 1             # Number of output variables (y-values) 
TARGETS = [0]            # Target values for output
GLOBAL_MIN = [[1, 1]]    # Global minima, if they exist.
  