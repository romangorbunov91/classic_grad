# version 0.1.2 by romangorbunov91
# 19-Aug-2025
import numpy as np

# Классический градиентный спуск.
def classic_grad_descent(loss_func, grad_func, x_init, learning_rate, tolerance, printoutput):
    # both 'x_init' and 'learning_rate' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = 10000000
    
    func_counter = 0
    grad_counter = 0
    
    x = x_init.copy()
    trajectory = []
    trajectory.append(x.copy())
    
    for i in range(iteration_max):
        grad = grad_func(x)
        grad_counter += 1
        
        x_prev = x.copy()
        
        x -= learning_rate * grad
        trajectory.append(x.copy())
        
        loss = loss_func(x)
        func_counter += 1
        
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

    return x, trajectory, i+1, func_counter, grad_counter


# Градиентный спуск с дроблением шага по условию Армихо.
def armijo_grad_descent(loss_func, grad_func, x_init, lr_multiplier, lr_coeff, tolerance, printoutput):
    # both 'x_init' and 'learning_rate_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = 10000000
    
    x = x_init.copy()
    trajectory = []
    trajectory.append(x.copy())
    
    loss = loss_func(x)
    grad = grad_func(x)
    func_counter = 1
    grad_counter = 1
    
    grad_norm = np.linalg.norm(grad, ord=None, axis=None)
    
    for i in range(iteration_max):
        learning_rate = np.array([1.0, 1.0])
        while (loss - loss_func(x - learning_rate * grad)) < lr_coeff * learning_rate[0] * grad_norm**2:
            func_counter += 1
            learning_rate *= lr_multiplier
        # One more increment.
        func_counter += 1
        
        x_prev = x.copy()
        x -= learning_rate * grad
        trajectory.append(x.copy())
        
        loss = loss_func(x)
        func_counter += 1

        grad = grad_func(x)
        grad_counter += 1
        
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

    return x, trajectory, i+1, func_counter, grad_counter