#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './antennacat_set/antennacat_function1/configs_F.py'
#   configurations for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: October 17, 2024
##-------------------------------------------------------------------------------\



import sys

try: # for outside func calls
    sys.path.insert(0, './src/objective_funcs/antennacat_set/')
    from antennacat_set.antennacat_function10_3_var_2_obj.func_F import func_F
    from antennacat_set.antennacat_function10_3_var_2_obj.constr_F import constr_F

except: # for local
    from func_F import func_F
    from constr_F import constr_F

OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "antennacat_func10_3_in_2_out.func_F"
CONSTR_FUNC_NAME = "antennacat_func10_3_in_2_out.constr_F"

# problem dependent variables
LB = [[0, 0, 0]]        # Lower boundaries for input
UB = [[1, 1, 1]]        # Upper boundaries for input
IN_VARS = 3                  # Number of input variables (x-values)
OUT_VARS = 2                  # Number of output variables (y-values)
TARGETS = [1.0, 1.0]     # Target values for output, on pareto front
GLOBAL_MIN = None    # Global minima, if they exist
