#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/fonseca_fleming_gen/graph.py'
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
# lower and upper bounds: LB = -4, UB= 4 for all cases
LOWER_BOUNDS = f_c.LB[0]
UPPER_BOUNDS = f_c.UB[0]
LB_x = LOWER_BOUNDS[0] 
UB_x = UPPER_BOUNDS[0] 
LB_y = LOWER_BOUNDS[1]
UB_y = UPPER_BOUNDS[1]
# objective function and constr are the same for all cases
FUNC_F = f_c.OBJECTIVE_FUNC
CONSTR_F = f_c.CONSTR_FUNC

# The F_F function can be used for 1:n variables.
MIN_DIM = 5
MAX_DIM = 5 # No given upper limit
NUM_SAMPLES = 1
NUM_DIENSIONS = np.linspace(MIN_DIM, MAX_DIM, NUM_SAMPLES)
NUM_ROW = 3  # For subplots
NUM_COL = 2  # For subplots
NUM_POINTS = 40 # Number of points for each dimension

#for exporting df to csv
filename = 'FF_pareto_coords_output.csv'
plotname = 'FF_output.png'


def pareto_front(X, Y, minimize=True):
    pareto_front_X = []
    pareto_front_Y = []

    ctr = 0
    if minimize:
        # Find Pareto front for minimizing objectives
        pareto_front_Y_max = float('inf')
        for x, y in sorted(zip(X, Y)):
            ctr = ctr + 1
            if (ctr%1e4) == 0:
                print("calculating pareto point:" + str(ctr))
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
    for _ in range(0, num_dim):
        # Define range and step size
        x = np.linspace(LB_x, UB_x, NUM_POINTS)
        x_dims.append(x)

    # Make into grid
    x_grid = np.array(np.meshgrid(*x_dims)).T.reshape(-1, num_dim) 
    print(x_grid.shape)

    # Evaluate function + apply constraints
    # this is the same function used by the optimizers, so the format reflects that
    paretoCoords = [] #col1: f1, col2: f2
    ctr = 0
    for c in x_grid:
        ctr = ctr + 1
        if (ctr%1e4)==0:
            print("objective func point: " + str(ctr))
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

        ax.set_xlabel('\t$f_{1}(...)$')
        ax.set_ylabel('$f_{2}(...)$')
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
df.to_csv(filename, index=False)  

# Save Plot
plt.savefig(plotname)

# # Show plot
# plt.show()
