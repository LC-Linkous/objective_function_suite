#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/DTLZ_N1_3_var_3_obj/graph.py'
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
LB_y = LOWER_BOUNDS[1]
UB_y = UPPER_BOUNDS[1]
LB_z = LOWER_BOUNDS[2]
UB_z = UPPER_BOUNDS[2]
IN_VARS = f_c.IN_VARS
OUT_VARS = f_c.OUT_VARS
FUNC_F = f_c.OBJECTIVE_FUNC
CONSTR_F = f_c.CONSTR_FUNC

# for exporting df to csv
filename = 'DTLZ_N1_3_var_3_obj_pareto_coords_output.csv'
plotname = 'DTLZ_N1_3_var_3_obj_plots.png'


def pareto_front(objectives, minimize=True):
    # pareto front is on the plane where x_i= 0.5 for all x_i in x_m
    pareto = []
    margin_of_error = 0.2
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



# Define range and step size
x = np.linspace(LB_x, UB_x, 30)
y = np.linspace(LB_y, UB_y, 30)
z = np.linspace(LB_z, UB_z, 30)

x_grid = np.array(np.meshgrid(x, y, z)).T.reshape(-1, IN_VARS) 

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
valid_x = validCoords[:,0]
valid_y = validCoords[:,1]
valid_z = validCoords[:,2]
# Convert paretoCoords to a NumPy array
paretoCoords = np.array(paretoCoords)
# Get the feasible objective space
objective_x = paretoCoords[:,0]
objective_y = paretoCoords[:,1]
objective_z = paretoCoords[:,2]
# Get the Pareto front from the feasible objective space
zipped_obj = list(zip(objective_x,objective_y, objective_z))
pareto = pareto_front(zipped_obj)

pareto = np.array(pareto)
print(pareto)

# Create figure and subplots
fig = plt.figure(figsize=(14, 6))

# 2D valid state space subplot - dimensionality reduction
ax1 = fig.add_subplot(121, projection='3d')
decision_space = ax1.tricontourf(valid_x, valid_y, valid_z, cmap='viridis')
ax1.set_xlabel('$x_1$')
ax1.set_ylabel('$x_2$')
ax1.set_zlabel('$x_3$')
ax1.set_title('Feasible Decision Space')

# 2D valid objective space subplot
ax2 = fig.add_subplot(122, projection='3d')
# check if the objective space is all pareto optimal
if len(pareto) < 1:
    # the objective space on this problem IS the Pareto front
    objective_space = ax2.scatter(objective_x.flatten(), objective_y.flatten(), objective_z.flatten(), s=5, marker = 'o', color='c', alpha=0.1)
    #ax2.scatter(objective_x.flatten(), objective_y.flatten(), objective_z.flatten(), marker='*', color='black') 

else: # not pareto optimal
    objective_space = ax2.scatter(objective_x.flatten(), objective_y.flatten(), objective_z.flatten(), s=5, marker = 'o', color='c', alpha=0.1)
    ax2.scatter(pareto[:,0],pareto[:,1], pareto[:,2], marker='*', color='black')

ax2.set_xlabel('$f_{1}(x_1,x_2,x_3)$')
ax2.set_ylabel('$f_{2}(x_1,x_2,x_3)$')
ax2.set_zlabel('$f_{3}(x_1,x_2,x_3)$')
ax2.set_title('Pareto Front & Feasible Objective Space')

#data frame for getting the coords for the various pareto fronts
df = pd.DataFrame({})

# Add two new columns to the dataframe
if len(pareto) > 0:
    x_col = "x"
    y_col = "y"
    z_col = "z"
    df_loop = pd.DataFrame({x_col: pareto[:,0],
                            y_col: pareto[:,1],
                            z_col: pareto[:,2]}) #not looped, but using name for consistency
    df = pd.concat([df, df_loop], axis=1) 

# Write DataFrame to CSV
df.to_csv(filename, index=False)  

# Adjust layout
plt.tight_layout()

# Save Plot
plt.savefig(plotname)

# Show plot
plt.show()
