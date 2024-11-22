'''
25. Crie um array bidimensional 4×3 com números inteiros aleatórios entre 1 e
10. Calcule:
a. A soma de todos os elementos.
b. O produto dos elementos em cada linha.
'''
import numpy as np

arr = np.random.randint(1, 10, 12).reshape(4, 3)
print(arr)
#a
soma = arr.sum()
print(soma)
#b
produtos = np.array([])
for i in arr:
    produtos = np.append(produtos, i.prod())
print(produtos)