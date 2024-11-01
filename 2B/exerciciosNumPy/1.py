#1. Crie dois arrays Numpy de 10 elementos cada, preenchidos com numeros inteiros aleatorios.
# Calcule a soma, a diferença, o produto e a divisão element-wise entre eles.
import numpy as np

array = np.random.randint(1, 100, size=10)
array2 = np.random.randint(1, 100, size=10)

soma = np.add(array, array2)
diff = np.subtract(array, array2)
product = np.multiply(array, array2)
div = np.divide(array, array2)
print(array)
print(array2)
print(soma)
print(diff)
print(product)
print(div)