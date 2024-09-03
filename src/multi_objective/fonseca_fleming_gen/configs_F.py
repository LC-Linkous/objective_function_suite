#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/fonseca_fleming_gen/configs_F.py'
#   configurations for function compatable with project optimizers
#
#   CONFIGURE TARGETS PRIOR TO USE
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 19, 2024
##-------------------------------------------------------------------------------\

import sys
try: # for outside func calls
    sys.path.insert(0, './optimizer-benchmarking/src/objective_funcs/multi_objective/')
    from objective_funcs.multi_objective.fonseca_fleming_gen.func_F import func_F
    from objective_funcs.multi_objective.fonseca_fleming_gen.constr_F import constr_F
except: # for local
    from func_F import func_F
    from constr_F import constr_F


OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "fonseca_fleming_gen.func_F"
CONSTR_FUNC_NAME = "fonseca_fleming_gen.constr_F"

# problem dependent variables
LB = [[-4, -4]]        # Lower boundaries for input
UB = [[4, 4]]          # Upper boundaries for input
IN_VARS = 2            # Number of input variables (x-values)
OUT_VARS = 2           # Number of output variables (y-values)
TARGETS = [0, 1]       # Target values for output, default
GLOBAL_MIN = None      # Global minima, if they exist.
# # 1 var, target on pareto front
# TARGETS = [0.00119898,0.71479384]
# # 2 var, target on pareto front
# TARGETS = [0.00353221,0.92691954]
# # 3 var, target on pareto front
# TARGETS = [0.00246980,0.98502516]
# # 4 var, target on pareto front
# TARGETS = [0.00540516,0.99325342] 
# # 5 var, target on pareto front
# TARGETS = [0.03910208,0.99956401] 
# # 6 var, target on pareto front
# TARGETS = [0.04673707,0.99990724] 
