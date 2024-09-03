#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/osyczka_kundu_6_vars/configs_F.py'
#   configurations for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 25, 2024
##-------------------------------------------------------------------------------\

import sys
try: # for outside func calls
    sys.path.insert(0, './optimizer-benchmarking/src/objective_funcs/multi_objective/')
    from objective_funcs.multi_objective.osyczka_kundu_6_vars.func_F import func_F
    from objective_funcs.multi_objective.osyczka_kundu_6_vars.constr_F import constr_F
except: # for local
    from func_F import func_F
    from constr_F import constr_F

OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "osyczka_kundu_6_vars.func_F"
CONSTR_FUNC_NAME = "osyczka_kundu_6_vars.constr_F"

# problem dependent variables
LB = [[0, 0, 1, 0, 1, 0]]       # Lower boundaries for input
UB = [[10, 10, 5, 6, 5, 10]]    # Upper boundaries for input
IN_VARS = 6                     # Number of input variables (x-values). This requires 6.
OUT_VARS = 2                    # Number of output variables (y-values)
TARGETS = [-164.24489796, 50.0] # Target values for output, on pareto front
GLOBAL_MIN = None               # Global minima, if they exist