# Классический градиентный спуск
## Квадратичная функция двух аргументов

$$\begin{equation}
    f(x_1, x_2) = a_{11} x_1^2 + (a_{12} + a_{21}) x_1 x_2 + a_{22} x_2^2 + b_1 x_1 + b_2 x_2 + c
\end{equation}$$

в векторной форме записи:

$$\begin{equation}
    f(x_1, x_2) = \vec{x}^T A \vec{x} + B^T \vec{x} + c,
\end{equation}$$

где $A$ - квадратная матрица размера $N=2$,

$$\begin{equation}
   B = \begin{bmatrix}
        b_1 \\
        b_2
    \end{bmatrix},
\end{equation}$$

$$\begin{equation}
   \vec{x} = \begin{bmatrix}
        x_1 \\
        x_2
    \end{bmatrix},
\end{equation}$$

$c$ - вещественное число.

## Функция Розенброка

$$\begin{equation}
    f(x_1, x_2) = (a - x_1)^2 + b (x_2 - x_1^2)^2.
\end{equation}$$

Минимум функции имеет место при ${(x_1, x_2)=(a, a^2)}$, причем ${f(a, a^2) = 0}$.

В большинстве случаев принимают ${a = 1}$, ${b = 100}$. Тогда минимум функции расположен в точке ${(1, 1)}$.