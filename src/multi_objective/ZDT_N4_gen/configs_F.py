#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/ZDT_N4_gen/configs_F.py'
#   configurations for function compatable with project optimizers
#
#   CONFIGURE TARGETS PRIOR TO USE
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 25, 2024
##-------------------------------------------------------------------------------\

import sys
try: # for outside func calls
    sys.path.insert(0, './optimizer-benchmarking/src/objective_funcs/multi_objective/')
    from objective_funcs.multi_objective.ZDT_N4_gen.func_F import func_F
    from objective_funcs.multi_objective.ZDT_N4_gen.constr_F import constr_F
except: # for local
    from func_F import func_F
    from constr_F import constr_F

OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "ZDT_N4_gen.func_F"
CONSTR_FUNC_NAME = "ZDT_N4_gen.constr_F"

# problem dependent variables
LB = [[0, -5,]]    # Lower boundaries for input
UB = [[1, 5]]      # Upper boundaries for input
IN_VARS = 2        # Number of input variables (x-values)
OUT_VARS = 2       # Number of output variables (y-values)
TARGETS = [0, 0]   # Target values for output, out of bounds. default
GLOBAL_MIN = None  # Global minima, if they exist
# # 2 var, target on pareto front
# TARGETS = [0.0, 1.34240807]
# # 3 var, target on pareto front
# TARGETS = [0.0, 4.58815248]
# # 4 var, target on pareto front
# TARGETS = [0, 6.38222873] 
# # 5 var, target on pareto front
# TARGETS = [0, 8.17630497] 
# # 6 var, target on pareto front
# TARGETS = [0, 9.97038121] 
# # 7 var, target on pareto front
# TARGETS = [0, 11.76445745] 