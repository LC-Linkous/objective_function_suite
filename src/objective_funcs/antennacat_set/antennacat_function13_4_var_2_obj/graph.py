#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './antennacat_set/antennacat_function1/graph.py'
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
LB_x = LOWER_BOUNDS[0] #all have the same lower and upper bounds
UB_x = UPPER_BOUNDS[0] 
IN_VARS = f_c.IN_VARS
OUT_VARS = f_c.OUT_VARS
FUNC_F = f_c.OBJECTIVE_FUNC
CONSTR_F = f_c.CONSTR_FUNC

MIN_DIM = 1
NUM_SAMPLES = 4
NUM_DIENSIONS = np.linspace(MIN_DIM, IN_VARS, NUM_SAMPLES)
NUM_POINTS = 20 # Number of points for each dimension


# for exporting df to csv
filename = 'antennacat_function13_4_var_2_obj_pareto_coords_output.csv'
plotname = 'antennacat_function13_4_var_2_obj_plots.png'


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

    # Create dynamic list of input vals
x_dims = []
for _ in range(0, IN_VARS):
    # Define range and step size
    x = np.linspace(LB_x, UB_x, NUM_POINTS)
    x_dims.append(x)

# Make into grid
x_grid = np.array(np.meshgrid(*x_dims)).T.reshape(-1, IN_VARS) 
print(x_grid.shape)

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
            paretoCoords.append(objective_space)




# Convert validCoords to a NumPy array
validCoords = np.array(validCoords)
print(validCoords)
valid_x = validCoords[:,0]
valid_y = validCoords[:,1]
valid_z = validCoords[:,2]
valid_a = validCoords[:,3] 
# Convert paretoCoords to a NumPy array
paretoCoords = np.array(paretoCoords)
# Get the feasible objective space
objective_x = paretoCoords[:,0]
objective_y = paretoCoords[:,1]
# Get the Pareto front from the feasible objective space
pareto_x, pareto_y = pareto_front(objective_x,objective_y)

print(paretoCoords)

# Create figure and subplots
fig = plt.figure(figsize=(14, 6))

# 2D valid state space subplot - dimensionality reduction
ax1 = fig.add_subplot(121, projection='3d')
plt.xticks(fontsize = 10) 
plt.yticks(fontsize = 10) 
x = np.multiply(valid_x,valid_a)

decision_space = ax1.tricontourf(x, valid_y, valid_z, cmap='viridis')
ax1.set_xlabel('$x_1$*$x_4$', fontsize = 10)
ax1.set_ylabel('$x_2$', fontsize = 10)
ax1.set_zlabel('$x_3$', fontsize = 10)
ax1.set_title('Function 13: 4 Input (Reduced 3D) Feasible Decision Space', fontsize = 15)


# 2D valid objective space subplot
ax2 = fig.add_subplot(122)
plt.xticks(fontsize = 10) 
plt.yticks(fontsize = 10) 
# check if the objective space is all pareto optimal
if len(pareto_x) < 1:
    # the objective space on this problem IS the Pareto front
    objective_space = ax2.scatter(objective_x.flatten(), objective_y.flatten(), color='c')
    ax2.scatter(objective_x.flatten(), objective_y.flatten(), marker='*', color='black')
else: # not pareto optimal
    objective_space = ax2.scatter(objective_x.flatten(), objective_y.flatten(), color='c')
    ax2.scatter(pareto_x, pareto_y, marker='*', color='black')

ax2.set_xlabel('$f_{1}(x_1,x_2,x_3,x_4)$')
ax2.set_ylabel('$f_{2}(x_1,x_2,x_3,x_4)$')
ax2.set_title('Function 13: Pareto Front & Feasible Objective Space')


#data frame for getting the coords for the various pareto fronts
df = pd.DataFrame({})

# # Add two new columns to the dataframe
# if len(pareto) > 0:
#     x_col = "x"
#     y_col = "y"
#     z_col = "z"
#     df_loop = pd.DataFrame({x_col: pareto[:,0],
#                             y_col: pareto[:,1],
#                             z_col: pareto[:,2]}) #not looped, but using name for consistency
#     df = pd.concat([df, df_loop], axis=1) 

# Write DataFrame to CSV
df.to_csv(filename, index=False)  

# Adjust layout
plt.tight_layout()

# Save Plot
plt.savefig(plotname)

# Show plot
plt.show()
