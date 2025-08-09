# version 0.1 by romangorbunov91
# 08-Aug-2025
import numpy as np
from IPython.display import clear_output

# Классический градиентный спуск.
def classic_grad_descent(loss_func, grad_func, x, learning_rate, tolerance):
    
    iteration_max = 200000
    
    func_counter = 0
    grad_counter = 0
    
    losses = []
    
    for i in range(iteration_max):
        grad = grad_func(x)
        grad_counter += 1
        
        x_prev = x.copy()
        
        x -= learning_rate * grad
        
        loss = loss_func(x)
        func_counter += 1
        losses.append(loss)
        
        x_norm = np.linalg.norm((x - x_prev), ord=None, axis=None)
        
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

    return x, losses, iter_final, func_counter, grad_counter