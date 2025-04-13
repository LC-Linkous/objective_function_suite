#! /usr/bin/python3

##--------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './antenna_model_objectives/half_wave_dipole/configs_F.py'
#   Constant values for objective function. Formatted for
#       automating objective function integration
#
#
#   Author(s): Lauren Linkous, Jonathan Lundquist
#   Last update: May 25, 2024
##--------------------------------------------------------------------\
import sys
try: # for outside func calls
    sys.path.insert(0, './src/objective_funcs/antenna_model_objectives/')
    from antenna_model_objectives.half_wave_dipole.func_F import func_F
    from antenna_model_objectives.half_wave_dipole.constr_F import constr_F
except: # for local
    from func_F import func_F
    from constr_F import constr_F

OBJECTIVE_FUNC = func_F
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "half_wave_dipole.func_F"
CONSTR_FUNC_NAME = "half_wave_dipole.constr_F"

# problem dependent variables
## variables are [LENGTH, WIRE RAD (optional)] in mm
## lower is bounded to 5mm, upper is bounded to create a large search area
## because this is a real-world based model, bounds need to reflect the selected target

# JUST THE LENGTH OF THE WIRE
LB = [[5]]           # Lower boundaries for input
UB = [[1e3]]         # Upper boundaries for input
## problem dimensions
IN_VARS = 1                 # Number of input variables (x-values)
OUT_VARS = 1                # Number of output variables (y-values)

# # LENGTH and AREA
# LB = [[5, 0.01]]        # Lower boundaries for input
# UB = [[1e3, 5]]         # Upper boundaries for input
# ## problem dimensions
# IN_VARS = 2                 # Number of input variables (x-values)
# OUT_VARS = 1                # Number of output variables (y-values)

## default target is 2.4 GHz
TARGETS = [2.4e9]           # Target values for output
GLOBAL_MIN = None           # Global minima, if they exist