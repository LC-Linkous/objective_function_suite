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
MAX_DIM = 4 
NUM_SAMPLES = 4
NUM_DIENSIONS = np.linspace(MIN_DIM, MAX_DIM, NUM_SAMPLES)
NUM_POINTS = 25 # Number of points for each dimension


# for exporting df to csv
filename = 'antennacat_function10_4_var_1_obj_pareto_coords_output.csv'
plotname = 'antennacat_function10_4_var_1_obj_plots.png'


def pareto_front(objectives, minimize=True):
    # pareto front is on the plane where x_i= 0.5 for all x_i in x_m
    pareto = []
    margin_of_error = 0.05
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
for _ in range(0, MAX_DIM):
    # Define range and step size
    x = np.linspace(LB_x, UB_x, NUM_POINTS)
    x_dims.append(x)

# Make into grid
x_grid = np.array(np.meshgrid(*x_dims)).T.reshape(-1, MAX_DIM) 
print(x_grid.shape)

# Evaluate function + apply constraints
# this is the same function used by the optimizers, so the format reflects that
validCoords = [] # the valid x,y coordinates
paretoCoords = [] #col1: f1, col2: f2
validObjective = []
for c in x_grid:
    # check if point is in the constraints.
    point_is_valid = CONSTR_F(c)
    if point_is_valid == True:
        # add point to validCoords
        validCoords.append(c)
        
        # pass point to the function to get the minimized F set
        objective_space, noErr = FUNC_F(c, OUT_VARS)
        if noErr == True:
            validObjective.append(objective_space)


# Convert validCoords to a NumPy array
validCoords = np.array(validCoords)
valid_x = validCoords[:,0]
valid_y = validCoords[:,1]
valid_z = validCoords[:,2]
valid_a = validCoords[:,3] 


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
ax1.set_title('Function 10: 4 Input (Reduced 3D) Feasible Decision Space', fontsize = 15)

validObjective = np.asarray(validObjective)

# 2D valid objective space subplot
ax2 = fig.add_subplot(122)
plt.xticks(fontsize = 10) 
plt.yticks(fontsize = 10) 
yfiller = np.multiply(validObjective,0)
ax2.scatter(validObjective.flatten(), yfiller.flatten(), s=5, marker = 'o', color='c', alpha=0.1)
ax2.set_xlabel('$f_{1}(x_1,x_2,x_3,x_4)$', fontsize = 10)
ax2.set_ylabel('filler_values', fontsize = 10)
ax2.set_title('Function 10: 1 Output Feasible Objective Space', fontsize = 15)

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
