'''
21. Crie:
a. Um array de zeros com tamanho 10.
b. Um array de uns com tamanho 5.
c. Uma matriz identidade 4×4.
'''
import numpy as np

#a
arr = np.repeat([0], 10)
print(arr)
#b
arr2 = np.repeat([1], 5)
print(arr2)
#c
arr3 = np.repeat([0], 16).reshape(4, 4)
arr3 = np.asmatrix(arr3)
print(arr3)