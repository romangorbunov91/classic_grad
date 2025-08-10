# version 0.1 by romangorbunov91
# 10-Aug-2025
import numpy as np

def f_well(x):
    return 0.8 * x[0]**2 + 1.2 * x[1]**2 + 0.4 * x[0]*x[1]

def f_poor(x):
    return 2 * x[0]**2 + 205 * x[1]**2 - 10 * x[0]*x[1] + 20 * x[0] + 30 * x[1] + 23

def f_rozen(x):
    return (1-x[0])**2 + 100 * (x[1]-x[0]**2)**2


def grad_well(x):
    return np.array([1.6*x[0] + 0.4*x[1],
                     0.4*x[0] + 2.4*x[1]])

def grad_poor(x):
    return np.array([4*x[0] - 10*x[1] + 20,
                     -10*x[0] + 410*x[1] + 30])

def grad_rozen(x):
    return np.array([400*x[0]**3 + 2*x[0] - 400*x[0]*x[1] - 2,
                     -200*x[0]**2 + 200*x[1]])