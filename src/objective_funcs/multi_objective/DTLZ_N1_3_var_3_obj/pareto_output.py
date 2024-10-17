#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/DTLZ_N1_3_var_4_obj/graph.py'
#   generates graphs for function based on constraints and configurations
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 25, 2024
##-------------------------------------------------------------------------------\


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import configs_F as f_c
# problem constraints - pulled from the function configs for the optimizers
LOWER_BOUNDS = f_c.LB[0]
UPPER_BOUNDS = f_c.UB[0]
LB_x = LOWER_BOUNDS[0]
UB_x = UPPER_BOUNDS[0] 
IN_VARS = f_c.IN_VARS
OUT_VARS = f_c.OUT_VARS
FUNC_F = f_c.OBJECTIVE_FUNC
CONSTR_F = f_c.CONSTR_FUNC

NUM_POINTS = 20 # Number of points for each dimension

# for exporting df to csv
filename = 'DTLZ_N1_3_var_4_obj_pareto_coords_output.csv'

def pareto_front(objectives, minimize=True):
    # pareto front is on the plane where x_i= 0.5 for all x_i in x_m
    pareto = []
    margin_of_error = 0.2 # margin of error is just for plotting purposes
    if minimize:
        # Find Pareto front for minimizing objectives
        for i in range(len(objectives)):
            is_pareto = True
            for j in objectives[i]:
                if abs(j - 0.5) > margin_of_error:
                    is_pareto = False
            if is_pareto:
                pareto.append(objectives[i])

    return pareto


# Create dynamic list of input vals
x_dims = []
for _ in range(0, IN_VARS):
    # Define range and step size
    x = np.linspace(LB_x, UB_x, NUM_POINTS)
    x_dims.append(x)

x_dims = np.asarray(x_dims)

# Make into grid
x_grid = np.array(np.meshgrid(*x_dims)).T.reshape(-1, IN_VARS) 

# Evaluate function + apply constraints
# this is the same function used by the optimizers, so the format reflects that
validCoords = [] # the valid x,y coordinates
paretoCoords = [] #col1: f1, col2: f2
for c in x_grid:
    # check if point is in the constraints.
    point_is_valid = CONSTR_F(c)
    if point_is_valid == True:
        # add point to validCoords
        validCoords.append(c)
        # pass point to the function to get the minimized F set
        objective_space, noErr = FUNC_F(c, OUT_VARS)

        if noErr == True:
            # coords to be evaluated as pareto front
            paretoCoords.append(objective_space)


# Get the Pareto front from the feasible objective space
zipped_obj = list(paretoCoords)
pareto = pareto_front(zipped_obj)

pareto = np.array(pareto)
print(pareto)


df = pd.DataFrame(pareto)

# Write DataFrame to CSV
df.to_csv(filename, index=False)  
