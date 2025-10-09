import numpy as np


def f_2d(x_1, x_2):
    return (x_1**2 + x_2 - 11) ** 2 + (x_1 + x_2**2 - 7) ** 2


def grad_x_1(x_1, x_2):
    return 4 * x_1 * (x_1**2 + x_2 - 11) + 2 * (x_1 + x_2**2 - 7)


def grad_x_2(x_1, x_2):
    return 2 * (x_1**2 + x_2 - 11) + 4 * x_2 * (x_1 + x_2**2 - 7)


def find_minima(x_1, x_2):
    iteration_number = 0
    alpha = 0.0025
    tol = 1e-15
    dJdx_1, dJdx_2 = np.inf, np.inf

    v_x_1, v_x_2 = 0, 0
    beta = 0.8

    while iteration_number < 500 and np.linalg.norm([dJdx_1, dJdx_2]) > tol:

        dJdx_1 = grad_x_1(x_1, x_2)
        dJdx_2 = grad_x_2(x_1, x_2)

        v_x_1 = v_x_1 * beta + dJdx_1 * (1 - beta)
        x_1 = x_1 - alpha * v_x_1

        v_x_2 = v_x_2 * beta + dJdx_2 * (1 - beta)
        x_2 = x_2 - alpha * v_x_2
        x_1 = np.clip(x_1, -10, 10)
        x_2 = np.clip(x_2, -10, 10)

        iteration_number += 1

    return x_1, x_2


def solution():
    x_0, y_0 = map(float, input().split())
    minima_coordinates = find_minima(x_0, y_0)
    result = " ".join(map(str, minima_coordinates))
    print(result)


solution()
