# version 1.0.0 by romangorbunov91
# 06-Sep-2025
import numpy as np

# Классический градиентный спуск.
def const_step_grad_descent(loss_func, grad_func, x_init, learning_rate, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = 10000000
    
    grad_counter = 0
    
    x = x_init.copy()
    trajectory = []
    trajectory.append(x.copy())
    
    for i in range(iteration_max):
        grad = grad_func(x)
        grad_counter += 1
        
        x -= learning_rate * grad
        trajectory.append(x.copy())
        
        grad_norm = np.linalg.norm(grad, ord=None, axis=None)

        if (grad_norm < tolerance):
            if printoutput:
                print('Iteration:', i)
                print('x-values:', np.round(x,4))
                print('Gradient norm:', np.round(grad_norm,4))
            break
    if printoutput:
        print('Iteration:', i)
        print('x-values:', np.round(x,4))
        print('Gradient norm:', np.round(grad_norm,4))
    # always func_counter = 0
    return x, trajectory, i+1, 0, grad_counter


# Градиентный спуск с дроблением шага по условию Армихо.
def armijo_grad_descent(loss_func, grad_func, x_init, lr_multiplier, lr_coeff, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = 10000000
    
    x = x_init.copy()
    trajectory = []
    trajectory.append(x.copy())
    
    loss = loss_func(x)
    func_counter = 1
    
    grad = grad_func(x)
    grad_counter = 1
    
    grad_norm = np.linalg.norm(grad, ord=None, axis=None)
    
    for i in range(iteration_max):
        learning_rate = 1.0
        while (loss - loss_func(x - learning_rate * grad)) < lr_coeff * learning_rate * grad_norm**2:
            func_counter += 1
            learning_rate *= lr_multiplier
        # One more increment because of 'while'.
        func_counter += 1
        
        x -= learning_rate * grad
        trajectory.append(x.copy())
        
        # New loss, grad, and norm-value.
        loss = loss_func(x)
        func_counter += 1

        grad = grad_func(x)
        grad_counter += 1
        
        grad_norm = np.linalg.norm(grad, ord=None, axis=None)
        
        if (grad_norm < tolerance):
            if printoutput:
                print('Iteration:', i)
                print('x-values:', np.round(x,4))
                print('Gradient norm:', np.round(grad_norm,4))
                print('Loss:', np.round(loss,4))
            break
    if printoutput:
        print('Iteration:', i)
        print('x-values:', np.round(x,4))
        print('Gradient norm:', np.round(grad_norm,4))
        print('Loss:', np.round(loss,4))

    return x, trajectory, i+1, func_counter, grad_counter

# Метод золотого сечения.
def golden(f, x_min, x_max, max_iter, eps):
    
    # Constant.
    phi = (1 + np.sqrt(5)) / 2
    # Initial step.
    x_l = x_min
    x_r = x_max
    delta = (x_r - x_l)/phi
    x_center_l = x_r - delta
    x_center_r = x_l + delta
    f_l = f(x_center_l)
    f_r = f(x_center_r)

    # Function compute counter.
    counter = 2
    
    for k in range(max_iter):
        if f_l > f_r:
            f_l = f_r
            x_l = x_center_l
            x_center_l = x_center_r
            x_center_r = x_l + (x_r - x_l)/phi
            f_r = f(x_center_r)
        else:
            f_r = f_l
            x_r = x_center_r
            x_center_r = x_center_l
            x_center_l = x_r - (x_r - x_l)/phi
            f_l = f(x_center_l)

        counter += 1
        
        if (x_r - x_l) < eps:
            return (x_r + x_l)/2, k+1, counter
    print('Solution has not been found (')

# Наискорейший спуск с одномерным поиском методом золотого сечения.
def steepest_grad_descent(loss_func, grad_func, x_init, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = 10000000
    
    x = x_init.copy()
    trajectory = []
    trajectory.append(x.copy())
    
    func_counter = 0
    
    grad = grad_func(x)
    grad_counter = 1
       
    def loss_func_1D(lr):
        return loss_func(x - lr * grad)
    
    for i in range(iteration_max):
        learning_rate, _, counter = golden(loss_func_1D, x_min=1e-8, x_max=0.9, max_iter=1000, eps=1e-3)
        func_counter += counter
        
        x -= learning_rate * grad
        trajectory.append(x.copy())

        grad = grad_func(x)
        grad_counter += 1
        
        grad_norm = np.linalg.norm(grad, ord=None, axis=None)
        
        if (grad_norm < tolerance):
            if printoutput:
                print('Iteration:', i)
                print('x-values:', np.round(x,4))
                print('Gradient norm:', np.round(grad_norm,4))
            break
    if printoutput:
        print('Iteration:', i)
        print('x-values:', np.round(x,4))
        print('Gradient norm:', np.round(grad_norm,4))

    return x, trajectory, i+1, func_counter, grad_counter

# Метод сопряженных градиентов.
def conjugate_grad_descent(A, b, x_init, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = 100
    
    x_init = (np.matrix(x_init)).T
    x = x_init.copy()
    trajectory = []
    trajectory.append(x.T.copy())

    r = b.T - A * x
    r_prev = r.copy()
    p = r.copy()

    for i in range(iteration_max):
        learning_rate = ((r.T * r)/(p.T * A*p)).item()
        
        x += learning_rate * p
        trajectory.append(x.T.copy())

        r -= learning_rate * A * p
        beta = ((r.T * r)/(r_prev.T * r_prev)).item()
        r_prev = r.copy()
        p = r + beta * p
        p_norm = np.linalg.norm(p, ord=None, axis=None)
        
        if (p_norm < tolerance):
            if printoutput:
                print('Iteration:', i)
                print('x-values:', np.round(x,4))
                print('Gradient norm:', np.round(p_norm,4))
            break
    if printoutput:
        print('Iteration:', i)
        print('x-values:', np.round(x,4))
        print('Gradient norm:', np.round(p_norm,4))
    func_counter = 0
    grad_counter = 0
    return x, trajectory, i+1, func_counter, grad_counter