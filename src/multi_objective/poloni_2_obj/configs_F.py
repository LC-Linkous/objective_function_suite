#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/poloni_2_obj/configs_F.py'
#   configurations for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 25, 2024
##-------------------------------------------------------------------------------\

import numpy as np
import sys
try: # for outside func calls
    sys.path.insert(0, './optimizer-benchmarking/src/objective_funcs/multi_objective/')
    from objective_funcs.multi_objective.poloni_2_obj.func_F import func_F
    from objective_funcs.multi_objective.poloni_2_obj.constr_F import constr_F
except: # for local
    from func_F import func_F
    from constr_F import constr_F

OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "poloni_2_obj.func_F"
CONSTR_FUNC_NAME = "poloni_2_obj.constr_F"

# problem dependent variables
LB = [[-np.pi, -np.pi]]             # Lower boundaries for input
UB = [[np.pi, np.pi]]               # Upper boundaries for input
IN_VARS = 2                         # Number of input variables (x-values)
OUT_VARS = 2                        # Number of output variables (y-values)
TARGETS = [1.00159207, 27.98438668] # Target values for output, on pareto front
GLOBAL_MIN = None                   # Global minima, if they exist
