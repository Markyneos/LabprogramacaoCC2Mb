# 6. Crie um array NumPy de 100 elementos aleatórios. 
# Em seguida, transforme este array numa matriz 10x10 utilizando o reshape

import numpy as np
arr = np.random.randint(0, 100, size=100)
matriz = arr.reshape(10, 10)
print(arr)
print(matriz)
