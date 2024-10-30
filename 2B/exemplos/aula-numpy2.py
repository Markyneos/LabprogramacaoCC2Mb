import numpy as np

#shapes
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

print(arr.shape)

numeros = np.arange(15)
print(numeros)
numeros = numeros.reshape(3, 5)
print(numeros)


matriz = np.arange(18)
print(matriz)
lm = matriz.reshape(2, 3, -1)
print(lm)
print(lm.shape)
