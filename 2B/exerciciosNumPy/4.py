# 4. Crie um array 2D de forma (4,3) e um array 1D de forma (3,). 
# Utilize broadcasting para somar os dois arrays. Apresente o resultado.
# Ex.:
# arr = np.array([1, 2, 3])
# test = arr * 2
# https://numpy.org/doc/stable/user/basics.broadcasting.html
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 3, 4]])
print(arr1 + arr2)
