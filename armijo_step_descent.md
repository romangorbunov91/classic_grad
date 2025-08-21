# Градиентный спуск с дроблением шага по условию Армихо
## Критерий останова

$$\begin{equation}
    \|\nabla f(x_k)\| < \varepsilon.
\end{equation}$$

## Координаты минимума функции
<img src='readme_img/armijo_step_descent_img/x1_optim_Well-conditioned.png' style='width:100%; height:auto;'>
<img src='readme_img/armijo_step_descent_img/x2_optim_Well-conditioned.png' style='width:100%; height:auto;'>

## Количество итераций
<img src='readme_img/armijo_step_descent_img/iter_count_Well-conditioned.png' style='width:100%; height:auto;'>

## Количество вычислений функции
<img src='readme_img/armijo_step_descent_img/func_count_Well-conditioned.png' style='width:100%; height:auto;'>

## Количество вычислений градиента
<img src='readme_img/armijo_step_descent_img/grad_count_Well-conditioned.png' style='width:100%; height:auto;'>

# Приложение с таблицами

<!-- START_X_OPTIM --> 
## Координаты минимума функции
|    eps |   Well-conditioned (x1) |   Well-conditioned (x2) |   Poorly-conditioned (x1) |   Poorly-conditioned (x2) |   Rosenbrock (x1) |   Rosenbrock (x2) |
|-------:|------------------------:|------------------------:|--------------------------:|--------------------------:|------------------:|------------------:|
| 0.1    |            -0.02728     |            -0.000176    |                  -5.49485 |                 -0.207248 |          0.901651 |          0.812605 |
| 0.01   |            -0.0021824   |            -1.408e-05   |                  -5.51703 |                 -0.207738 |          0.988969 |          0.978014 |
| 0.001  |            -0.000174592 |            -1.1264e-06  |                  -5.51924 |                 -0.207787 |          0.998996 |          0.997989 |
| 0.0001 |            -3.46931e-05 |             3.51437e-05 |                  -5.51946 |                 -0.207792 |          0.999892 |          0.999784 |
| 1e-05  |            -2.77545e-06 |             2.81149e-06 |                  -5.51948 |                 -0.207792 |          0.999989 |          0.999978 |
<!-- END_X_OPTIM -->
<!-- START_ITER_COUNTER --> 
## Количество итераций
|    eps |   Well-conditioned |   Poorly-conditioned |   Rosenbrock |
|-------:|-------------------:|---------------------:|-------------:|
| 0.1    |                  5 |                  172 |          503 |
| 0.01   |                  7 |                  250 |          928 |
| 0.001  |                  9 |                  328 |         1063 |
| 0.0001 |                 10 |                  403 |         1175 |
| 1e-05  |                 12 |                  485 |         1325 |
<!-- END_ITER_COUNTER -->
<!-- START_FUNC_COUNTER --> 
## Количество вычислений функции
|    eps |   Well-conditioned |   Poorly-conditioned |   Rosenbrock |
|-------:|-------------------:|---------------------:|-------------:|
| 0.1    |                 19 |                 1656 |         5253 |
| 0.01   |                 25 |                 2404 |         9591 |
| 0.001  |                 31 |                 3152 |        10865 |
| 0.0001 |                 34 |                 3871 |        11900 |
| 1e-05  |                 40 |                 4657 |        13286 |
<!-- END_FUNC_COUNTER -->
<!-- START_GRAD_COUNTER --> 
## Количество вычислений градиента
|    eps |   Well-conditioned |   Poorly-conditioned |   Rosenbrock |
|-------:|-------------------:|---------------------:|-------------:|
| 0.1    |                  6 |                  173 |          504 |
| 0.01   |                  8 |                  251 |          929 |
| 0.001  |                 10 |                  329 |         1064 |
| 0.0001 |                 11 |                  404 |         1176 |
| 1e-05  |                 13 |                  486 |         1326 |
<!-- END_GRAD_COUNTER -->