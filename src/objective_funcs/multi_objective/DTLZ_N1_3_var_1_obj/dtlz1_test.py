import numpy as np
import matplotlib.pyplot as plt

def g_function(x):
    return 100 * (len(x) + np.sum((x - 0.5)**2 - np.cos(20 * np.pi * (x - 0.5))))

def dtlz1(X, NO_OF_OUTS):
    """
    Compute the DTLZ1 function values for given input vector X.

    Parameters:
    X : numpy.ndarray
        Input vector of decision variables.
    NO_OF_OUTS : int
        Number of objective functions.

    Returns:
    numpy.ndarray
        Array of objective function values.
    """
    n = len(X)  # Number of decision variables
    m = NO_OF_OUTS  # Number of objective functions
    
    g_value = g_function(X[m-1:])
    
    objectives = np.zeros(m)
    for i in range(m-1):
        product = np.prod(X[:m-i-1])
        objectives[i] = 0.5 * product * (1 + g_value)
    objectives[m-1] = 0.5 * (1 - X[0]) * (1 + g_value)
    
    return objectives

# Generate Pareto front points for visualization
def generate_pareto_front(n_points, NO_OF_OUTS):
    pareto_front = np.zeros((n_points, NO_OF_OUTS))
    for i in range(n_points):
        x = np.random.rand(NO_OF_OUTS)
        print(x)
        pareto_front[i] = dtlz1(x, NO_OF_OUTS)
    return pareto_front

# Example usage and plotting
NO_OF_OUTS_example = 2  # Example number of objective functions
pareto_front_points = generate_pareto_front(100, NO_OF_OUTS_example)


# Plotting
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(pareto_front_points[:, 0], pareto_front_points[:, 1], label='Pareto Front Points')
ax.set_xlabel('Objective 1')
ax.set_ylabel('Objective 2')
ax.set_title('Pareto Front for DTLZ1')
ax.legend()
plt.grid(True)
plt.show()
