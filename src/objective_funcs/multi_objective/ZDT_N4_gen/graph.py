#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/ZDT_N4_gen/graph.py'
#   generates graphs for function based on constraints and configurations
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: May 30, 2024
##-------------------------------------------------------------------------------\


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import configs_F as f_c
# problem constraints - pulled from the function configs for the optimizers
# lower and upper bounds: LB = 0, UB= 1 for all cases
LOWER_BOUNDS = f_c.LB[0]
UPPER_BOUNDS = f_c.UB[0]
LB_x1 = LOWER_BOUNDS[0]  # the first bounds are different
UB_x1 = UPPER_BOUNDS[0]  # the first bounds are different 
LB_xother = LOWER_BOUNDS[1] 
UB_xother = UPPER_BOUNDS[1] 
# objective function and constr are the same for all cases
FUNC_F = f_c.OBJECTIVE_FUNC
CONSTR_F = f_c.CONSTR_FUNC

# The ZDT_N4 function can be used for 2:10 variables.
MIN_DIM = 2
MAX_DIM = 3
NUM_SAMPLES = 2
NUM_DIENSIONS = np.linspace(MIN_DIM, MAX_DIM, NUM_SAMPLES)
NUM_ROW = 2  # For subplots
NUM_COL = 2  # For subplots
NUM_POINTS = 20 # Number of points for each dimension

#writing out the pareto front to a csv for comparison
filepath = "ZDT4_pareto_coords_output.csv"
plotname = "ZDT4_output.png"


def pareto_front(X, Y, minimize=True):
    pareto_front_X = []
    pareto_front_Y = []

    if minimize:
        # Find Pareto front for minimizing objectives
        pareto_front_Y_max = float('inf')
        for x, y in sorted(zip(X, Y)):
            if y < pareto_front_Y_max:
                pareto_front_X.append(x)
                pareto_front_Y.append(y)
                pareto_front_Y_max = y
    else:
        # Find Pareto front for maximizing objectives
        pareto_front_Y_min = float('-inf')
        for x, y in sorted(zip(X, Y), reverse=True):
            if y > pareto_front_Y_min:
                pareto_front_X.append(x)
                pareto_front_Y.append(y)
                pareto_front_Y_min = y

    return pareto_front_X, pareto_front_Y

def calculateParetoAndPlot(num_dim, fig, subplt_idx):

    # Create dynamic list of input vals
    x_dims = []
    for idx in range(0, num_dim):
        # Define range and step size
        if idx == 0:
            x = np.linspace(LB_x1, UB_x1, NUM_POINTS)
        else:
            x = np.linspace(LB_xother, UB_xother, NUM_POINTS)
        x_dims.append(x)

    # Make into grid
    x_grid = np.array(np.meshgrid(*x_dims)).T.reshape(-1, num_dim) 
    print(x_grid.shape)

    # Evaluate function + apply constraints
    # this is the same function used by the optimizers, so the format reflects that
    paretoCoords = [] #col1: f1, col2: f2
    for c in x_grid:
        # check if point is in the constraints.
        point_is_valid = CONSTR_F(c)
        if point_is_valid == True:
            # pass point to the function to get the minimized F set
            objective_space, noErr = FUNC_F(c)
            if noErr == True:
                paretoCoords.append(objective_space)


    # Convert paretoCoords to a NumPy array
    paretoCoords = np.array(paretoCoords)

    # Get the feasible objective space
    objective_x = paretoCoords[:,0]
    objective_y = paretoCoords[:,1]
    # Get the Pareto front from the feasible objective space
    pareto_x, pareto_y = pareto_front(objective_x,objective_y)

    # Create subplot
    ax = fig.add_subplot(NUM_ROW, NUM_COL, subplt_idx)
    # check if the objective space is all pareto optimal
    if len(pareto_x) < 1:
        # the objective space on this problem IS the Pareto front
        objective_space = ax.scatter(objective_x.flatten(), objective_y.flatten(), color='c')
        ax.scatter(objective_x.flatten(), objective_y.flatten(), marker='*', color='black')
    else: # not pareto optimal
        objective_space = ax.scatter(objective_x.flatten(), objective_y.flatten(), color='c')
        ax.scatter(pareto_x, pareto_y, marker='*', color='black')

        ax.set_xlabel('$f_{1}(x,y)$')
        ax.set_ylabel('$f_{2}(x,y)$')
        ax.set_title('$i$ = ' + str(num_dim))

    return pareto_x, pareto_y # for writing out to csv


# Create figure and subplots
fig = plt.figure(figsize=(16, 8))
plt.suptitle('Pareto Front & Feasible Objective Space')  # Set main figure title

dimension_list = NUM_DIENSIONS

#data frame for getting the coords for the various pareto fronts
df = pd.DataFrame({})

# iterate through the selected dimensions
ctr = 0
for dl in dimension_list:
    # increment counter
    ctr = ctr + 1
    # Calculate the object space and pareto front, plot
    pareto_x, pareto_y = calculateParetoAndPlot(int(dl), fig, ctr)
    # Add two new columns to the dataframe
    x_col = "x_" + str(int(dl))
    y_col = "y_" + str(int(dl))
    df_loop = pd.DataFrame({x_col: pareto_x,
                            y_col: pareto_y})
    df = pd.concat([df, df_loop], axis=1) 

# Write DataFrame to CSV
df.to_csv(filepath, index=False)  

# Adjust layout
plt.tight_layout()

# Save Plot
plt.savefig(plotname)

# Show plot
plt.show()
