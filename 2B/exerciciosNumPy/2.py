import numpy as np
#2. Crie duas matrizes 3x3 com numeros aleatorios. Realize a multiplicação de matrizes (dot product) e 
#calcule a transposta da matriz resultado.

# | a | b |   | x | y |   | a*x + b*z | a*y + b*w|
# | c | d | . | z | w | = | c*x + d*z | c*y + d*w|

# | 5 | 10 |    | 5  | 8 |
# | 8 | 3  |t = | 10 | 3 |

matriz = np.random.randint(1, 100, size=(3, 3))
matriz2 = np.random.randint(1, 100, size=(3, 3))

print(matriz)
print(matriz2)

mult = np.matmul(matriz, matriz2)
print(mult)

transpo = mult.transpose()
print(transpo)