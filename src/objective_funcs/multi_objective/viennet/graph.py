#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   '.src/objective_funcs/multi_objective/viennet/graph.py'
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
LB_x = LOWER_BOUNDS[0]
UB_x = UPPER_BOUNDS[0] 
LB_y = LOWER_BOUNDS[1]
UB_y = UPPER_BOUNDS[1]
FUNC_F = f_c.OBJECTIVE_FUNC
CONSTR_F = f_c.CONSTR_FUNC

# for exporting df to csv
filename = 'V_pareto_coords_output.csv'
plotname = 'viennet_plots.png'

def pareto_front(X, Y, Z, minimize=True):
    # Calculate Pareto front from the given objective space represented by arrays X, Y, and Z.
    pareto_front_X = []
    pareto_front_Y = []
    pareto_front_Z = []

    if minimize:
        # Find Pareto front for minimizing objectives
        for i in range(len(X)):
            is_pareto = True
            for j in range(len(X)):
                if i != j and X[j] <= X[i] and Y[j] <= Y[i] and Z[j] <= Z[i]:
                    is_pareto = False
                    break
            if is_pareto:
                pareto_front_X.append(X[i])
                pareto_front_Y.append(Y[i])
                pareto_front_Z.append(Z[i])
    else:
        # Find Pareto front for maximizing objectives
        for i in range(len(X)):
            is_pareto = True
            for j in range(len(X)):
                if i != j and X[j] >= X[i] and Y[j] >= Y[i] and Z[j] >= Z[i]:
                    is_pareto = False
                    break
            if is_pareto:
                pareto_front_X.append(X[i])
                pareto_front_Y.append(Y[i])
                pareto_front_Z.append(Z[i])
    return pareto_front_X, pareto_front_Y, pareto_front_Z



# Define range and step size
x = np.linspace(LB_x, UB_x, 100)
y = np.linspace(LB_y, UB_y, 100)
X, Y = np.meshgrid(x, y)

# Reshape X and Y to 1D arrays
X_flat = X.flatten()
Y_flat = Y.flatten()

# Stack X and Y to create coords as a 2D array
coords = np.stack((X_flat, Y_flat), axis=-1)

# Evaluate function + apply constraints
# this is the same function used by the optimizers, so the format reflects that

validCoords = [] # the valid x,y coordinates
paretoCoords = [] #col1: f1, col2: f2
for c in coords:
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
valid_x = validCoords[:,0]
valid_y = validCoords[:,1]
# Convert paretoCoords to a NumPy array
paretoCoords = np.array(paretoCoords)
# Get the feasible objective space
objective_x = paretoCoords[:,0]
objective_y = paretoCoords[:,1]
objective_z = paretoCoords[:,2]
# Get the Pareto front from the feasible objective space
pareto_x, pareto_y, pareto_z = pareto_front(objective_x,objective_y, objective_z)


# Create figure and subplots
fig = plt.figure(figsize=(14, 7))

# 2D valid state space subplot
ax1 = fig.add_subplot(121)
decision_space = ax1.scatter(valid_x, valid_y, marker='o', color='darkslateblue')
ax1.set_xlabel('$x_1$')
ax1.set_ylabel('$x_2$')
ax1.set_title('Feasible Decision Space')

# 2D valid objective space subplot
ax2 = fig.add_subplot(122, projection='3d')
# check if the objective space is all pareto optimal
if len(pareto_x) < 1:
    # the objective space on this problem IS the Pareto front
    objective_space = ax2.scatter(objective_x.flatten(), objective_y.flatten(), objective_z.flatten(), s=5, marker = 'o', color='c', alpha=0.1)
    ax2.scatter(objective_x.flatten(), objective_y.flatten(), objective_z.flatten(), marker='*', color='black') 
else: # not pareto optimal
    objective_space = ax2.scatter(objective_x.flatten(), objective_y.flatten(), objective_z.flatten(), s=5, marker = 'o', color='c', alpha=0.1)
    ax2.scatter(pareto_x, pareto_y, pareto_z, marker='*', color='black')

ax2.set_xlabel('$f_{1}(x_1,x_2)$')
ax2.set_ylabel('$f_{2}(x_1,x_2)$')
ax2.set_zlabel('$f_{3}(x_1,x_2)$')
ax2.set_title('Pareto Front & Feasible Objective Space')

#data frame for getting the coords for the various pareto fronts
df = pd.DataFrame({})

# Add two new columns to the dataframe
x_col = "x"
y_col = "y"
z_col = "z"
df_loop = pd.DataFrame({x_col: pareto_x,
                        y_col: pareto_y,
                        z_col: pareto_z}) #not looped, but using name for consistency
df = pd.concat([df, df_loop], axis=1) 

# Write DataFrame to CSV
df.to_csv(filename, index=False)  

# Adjust layout
plt.tight_layout()

# Save Plot
plt.savefig(plotname)

# Show plot
plt.show()
