#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/osyczka_kundu_6_vars/graph.py'
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
LOWER_BOUNDS = f_c.LB[0]
UPPER_BOUNDS = f_c.UB[0]
LB_x1 = LOWER_BOUNDS[0] 
UB_x1 = UPPER_BOUNDS[0]
LB_x2 = LOWER_BOUNDS[1] 
UB_x2 = UPPER_BOUNDS[1]
LB_x3 = LOWER_BOUNDS[2] 
UB_x3 = UPPER_BOUNDS[2]
LB_x4 = LOWER_BOUNDS[3] 
UB_x4 = UPPER_BOUNDS[3]
LB_x5 = LOWER_BOUNDS[4] 
UB_x5 = UPPER_BOUNDS[4]
LB_x6 = LOWER_BOUNDS[5] 
UB_x6 = UPPER_BOUNDS[5]

FUNC_F = f_c.OBJECTIVE_FUNC
CONSTR_F = f_c.CONSTR_FUNC
IN_VARS = f_c.IN_VARS


# for exporting df to csv
filename = 'OK6vars_pareto_coords_output.csv'
plotname = 'osyczka_kundu_6_vars_plots.png'

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



# Define range and step size - this function takes 6 inputs
x1 = np.linspace(LB_x1, UB_x1, 15)
x2 = np.linspace(LB_x2, UB_x2, 15)
x3 = np.linspace(LB_x3, UB_x3, 15)
x4 = np.linspace(LB_x4, UB_x4, 15)
x5 = np.linspace(LB_x5, UB_x5, 15)
x6 = np.linspace(LB_x6, UB_x6, 15)

x_grid = np.array(np.meshgrid(x1, x2, x3, x4, x5, x6)).T.reshape(-1, IN_VARS) 

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
        objective_space, noErr = FUNC_F(c)
        if noErr == True:
            paretoCoords.append(objective_space)


# Convert validCoords to a NumPy array
validCoords = np.array(validCoords)
valid_x1 = validCoords[:,0]
valid_x2 = validCoords[:,1]
valid_x3 = validCoords[:,2]
valid_x4 = validCoords[:,3]
valid_x5 = validCoords[:,4]
valid_x6 = validCoords[:,5]

# Convert paretoCoords to a NumPy array
paretoCoords = np.array(paretoCoords)

# Get the feasible objective space
objective_x = paretoCoords[:,0]
objective_y = paretoCoords[:,1]
# Get the Pareto front from the feasible objective space
pareto_x, pareto_y = pareto_front(objective_x,objective_y)

# Create figure and subplots
fig = plt.figure(figsize=(14, 7))

# 2D valid state space subplot - dimensionality reduction
ax1 = fig.add_subplot(121, projection='3d')
decision_space = ax1.tricontourf(np.multiply(valid_x1,valid_x2), np.multiply(valid_x3,valid_x5), np.multiply(valid_x4,valid_x6), cmap='viridis')
ax1.set_xlabel('x1*x2')
ax1.set_ylabel('x3*x5')
ax1.set_zlabel('x4*x6')
ax1.set_title('Feasible Decision Space')

# 2D valid objective space subplot
ax2 = fig.add_subplot(122)
# check if the objective space is all pareto optimal
if len(pareto_x) < 1:
    # the objective space on this problem IS the Pareto front
    objective_space = ax2.scatter(objective_x.flatten(), objective_y.flatten(), color='c')
    ax2.scatter(objective_x.flatten(), objective_y.flatten(), marker='*', color='black') #, cmap='viridis')
else: # not pareto optimal
    objective_space = ax2.scatter(objective_x.flatten(), objective_y.flatten(), color='c') #, z_vals.flatten(), cmap='ocean')
    ax2.scatter(pareto_x, pareto_y, marker='*', color='black')

ax2.set_xlabel('$f_{1}(x_1,....,x_6)$')
ax2.set_ylabel('$f_{2}(x_1,...,x_6)$')
ax2.set_title('Pareto Front & Feasible Objective Space')

#data frame for getting the coords for the various pareto fronts
df = pd.DataFrame({})

# Add two new columns to the dataframe
x_col = "x"
y_col = "y"
df_loop = pd.DataFrame({x_col: pareto_x,
                        y_col: pareto_y}) #not looped, but using name for consistency
df = pd.concat([df, df_loop], axis=1) 

# Write DataFrame to CSV
df.to_csv(filename, index=False)  

# Adjust layout
plt.tight_layout()

# Save Plot
plt.savefig(plotname)

# Show plot
plt.show()
