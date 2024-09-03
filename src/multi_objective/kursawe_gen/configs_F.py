#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/kursawe_gen/configs_F.py'
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
    from objective_funcs.multi_objective.kursawe_gen.func_F import func_F
    from objective_funcs.multi_objective.kursawe_gen.constr_F import constr_F
except: # for local
    from func_F import func_F
    from constr_F import constr_F

OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "kursawe_gen.func_F"
CONSTR_FUNC_NAME = "kursawe_gen.constr_F"

# problem dependent variables
LB = [[-5, -5]]        # Lower boundaries for input
UB = [[5, 5]]          # Upper boundaries for input
IN_VARS = -1           # Number of input variables (x-values)
OUT_VARS = 2           # Number of output variables (y-values)
TARGETS = [0, 0]       # Target values for output, out of bounds. default
GLOBAL_MIN = None      # Global minima, if they exist
# # 1 var, target on pareto front
# TARGETS = [-9.94987479,0.05241274]
# # 2 var, target on pareto front
# TARGETS = [-9.85816561,0.18223784]
# # 3 var, target on pareto front
# TARGETS = [-18.56540645,1.30443312]
# # 4 var, target on pareto front
# TARGETS = [-27.84810968,1.73924415] 
# # 5 var, target on pareto front
# TARGETS = [-37.1308129,1.99182297] 
# # 6 var, target on pareto front
# TARGETS = [-46.41351613,2.24440179] 
