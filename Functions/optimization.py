# version 0.4 by romangorbunov91
# 15-Aug-2025
import numpy as np

# Классический градиентный спуск.
def classic_grad_descent(loss_func, grad_func, x_init, learning_rate, tolerance, printoutput):
    # both 'x_init' and 'learning_rate' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = 10000000
    
    func_counter = 0
    grad_counter = 0
    
    losses = []
    
    x = x_init.copy()
    for i in range(iteration_max):
        grad = grad_func(x)
        grad_counter += 1
        
        x_prev = x.copy()
        
        x -= learning_rate * grad
        
        loss = loss_func(x)
        func_counter += 1
        losses.append(loss)
        
        x_norm = np.linalg.norm((x - x_prev), ord=None, axis=None)
        grad_norm = np.linalg.norm(grad, ord=None, axis=None)

        if (grad_norm < tolerance):
            if printoutput:
                print('Iteration:', i)
                print('x-values:', np.round(x,4))
                print('x-norm:', np.round(x_norm,4))
                print('Gradient norm:', np.round(grad_norm,4))
                print('Loss:', np.round(loss,4))
            break
    if printoutput:
        print('Iteration:', i)
        print('x-values:', np.round(x,4))
        print('x-norm:', np.round(x_norm,4))
        print('Gradient norm:', np.round(grad_norm,4))
        print('Loss:', np.round(loss,4))

    return x, losses, i+1, func_counter, grad_counter


# Градиентный спуск с дроблением шага по условию Армихо.
def armijo_grad_descent(loss_func, grad_func, x_init, learning_rate_init, lr_multiplier, tolerance, printoutput):
    # both 'x_init' and 'learning_rate_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = 10000000
    
    func_counter = 0
    grad_counter = 0
    
    losses = []
    
    x = x_init.copy()
    learning_rate = learning_rate_init.copy()
    
    for i in range(iteration_max):
        grad = grad_func(x)
        grad_counter += 1
        
        x_prev = x.copy()
        x -= learning_rate * grad
        
        loss = loss_func(x)
        func_counter += 1
        losses.append(loss)
        learning_rate *= lr_multiplier
        
        if i != 0:
            if (losses[-2] - losses[-1]) < tolerance * learning_rate[0] * grad_norm**2:
                if printoutput:
                    print('Iteration:', i)
                    print('x-values:', np.round(x,4))
                    print('x-norm:', np.round(x_norm,4))
                    print('Gradient norm:', np.round(grad_norm,4))
                    print('Loss:', np.round(loss,4))
                break
        
        # New norm-values.
        x_norm = np.linalg.norm((x - x_prev), ord=None, axis=None)
        grad_norm = np.linalg.norm(grad, ord=None, axis=None)
        
        if (grad_norm < tolerance):
            if printoutput:
                print('Iteration:', i)
                print('x-values:', np.round(x,4))
                print('x-norm:', np.round(x_norm,4))
                print('Gradient norm:', np.round(grad_norm,4))
                print('Loss:', np.round(loss,4))
            break
    if printoutput:
        print('Iteration:', i)
        print('x-values:', np.round(x,4))
        print('x-norm:', np.round(x_norm,4))
        print('Gradient norm:', np.round(grad_norm,4))
        print('Loss:', np.round(loss,4))

    return x, losses, i+1, func_counter, grad_counter