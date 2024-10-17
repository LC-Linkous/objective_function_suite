#! /usr/bin/python3

##-------------------------------------------------------------------------------\
#   Optimizer Benchmarking
#   './constrained_objective/rosenbrock_disk/constr_F.py'
#   constraints function for function compatable with project optimizers
#
#   Author(s): Lauren Linkous (LINKOUSLC@vcu.edu)
#   Last update: March 31, 2024
##-------------------------------------------------------------------------------\


import numpy as np

def constr_F(X, center=[0,0], lim=2):
    # returns F = True if the (X[0], X[1]) pair is within the constraints. Otherwise returns False.
    F = True #default
    # Calculate the distance between the point and the center of the circle
    distance = np.sqrt((X[0] - center[0])**2 + (X[1] - center[1])**2)
    edge = X[0]**2 + X[1]**2
    # Check if the edge is outside the limit
    if edge > lim:
        F = False
        return F
    # Check if the distance is less than or equal to the radius (inside the circle)
    F = (distance <= edge)
    return F