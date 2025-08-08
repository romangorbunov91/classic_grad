# version 0.1 by romangorbunov91
# 08-Aug-2025
import numpy as np
from IPython.display import clear_output
import time

# Классический градиентный спуск.
def classic_grad(loss_func, grad_func, x, learning_rate, tolerance):
    time_init = time.time()
    
    iteration_max = 200000
    
    losses = []
    
    for i in range(iteration_max):
        grad = grad_func(x)
        x_prev = x.copy()
        
        x -= learning_rate * grad
        
        x_norm = np.linalg.norm((x - x_prev), ord=None, axis=None)
        
        loss = loss_func(x)
        losses.append(loss)
        
        if i % 100 == 0:
            clear_output(wait=True)
            print('Iteration:', i)
            print('x-values:', np.round(x,4))
            print('x-norm:', np.round(x_norm,4))
            print('Gradient:', np.round(grad,4))
            print('Loss:', np.round(loss,4))
            
        if (x_norm < tolerance):
            print('Iteration:', i)
            print('x-values:', np.round(x,4))
            print('x-norm:', np.round(x_norm,4))
            print('Gradient:', np.round(grad,4))
            print('Loss:', np.round(loss,4))
            break
    
    iter_final = i
    fit_time = time.time() - time_init
    return x, losses, iter_final, fit_time