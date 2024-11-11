from laplace import laplace
import numpy as np

#Exercício Cramer
sistema = np.array([
    [1, 2, 1, 12],
    [1, -3, 5, 1],
    [2, -1, 3, 10]
])

def cramer(mat) -> int:
    result = 0

    return result