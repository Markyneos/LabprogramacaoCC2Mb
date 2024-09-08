def rotacionar_matriz_90(matriz):
  matriz2 = [[j for j in range(len(matriz[i]))] for i in range(len(matriz))]
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
     matriz2[i][-j] = matriz[j - 1][i]
  return matriz2

def print_matrix(mat):
  for row in mat:
    print(" ".join(str(n) for n in row))

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print_matrix(rotacionar_matriz_90(matriz))

