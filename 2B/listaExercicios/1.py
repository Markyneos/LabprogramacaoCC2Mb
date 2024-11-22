'''
1. Crie um array NumPy contendo os números de 1 a 10. Em seguida,
transforme-o em um array bidimensional com 2 linhas e 5 colunas.
'''
import numpy as np

arr = np.arange(1, 11)
print(arr)
arr.resize(2, 5)
print(arr)
